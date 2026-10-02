import cv2
import numpy as np
import matplotlib.pyplot as plt

def process_signature_roi(image_path, roi_coords, roi_name="ROI"):
    # 1. Load Citra & Crop Area ROI
    img = cv2.imread(image_path)
    if img is None:
        print(f"Gagal memuat citra: {image_path}")
        return None
    
    h, w, _ = img.shape
    y1, y2 = int(roi_coords[0] * h), int(roi_coords[1] * h)
    x1, x2 = int(roi_coords[2] * w), int(roi_coords[3] * w)
    
    roi = img[y1:y2, x1:x2]
    
    # 2. Konversi ke Grayscale
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    # Preprocessing: Blur ringan untuk mengurangi noise tingkat piksel
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)


    
    # 3. Penerapan Metode Thresholding (Binary Inverted: Foreground = 255, Background = 0)
    
    # A. Global Thresholding
    _, thresh_global = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY_INV)

    
    # B. Otsu Thresholding
    _, thresh_otsu = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)


    # C. Adaptive Thresholding (Gaussian)
    thresh_adaptive = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 21, 10
    )
    
    # Gunakan Otsu/Adaptive sebagai masukan morfologi (Otsu optimal untuk dokumen cetak)
    binary_base = thresh_otsu


    
    # 4. Morphological Operations
    kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    
    # Opening: Mereduksi noise bercak kecil/bintik-bintik
    opened = cv2.morphologyEx(binary_base, cv2.MORPH_OPEN, kernel_open)
    
    # Closing: Menghubungkan goresan pena tanda tangan yang terputus
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel_close)

    
    # 5. Perhitungan Karakteristik / Fitur Foreground
    total_pixels = closed.size
    fg_pixels = cv2.countNonZero(closed)
    fg_density = fg_pixels / total_pixels
    
    # Perhitungan Connected Components untuk memfilter objek terlalu kecil
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(closed)
    # Exclude background (label 0)
    component_sizes = stats[1:, cv2.CC_STAT_AREA] if num_labels > 1 else [0]
    valid_components = [size for size in component_sizes if size > 15] # Filter noise minimal
    
    # 6. Aturan Keputusan (Decision Rule)
    # Tanda tangan memiliki jumlah piksel foreground dan komponen terhubung yang cukup
    MIN_FG_PIXELS = 300       # Minimal jumlah piksel goresan
    MIN_DENSITY = 0.015       # Minimal 1.5% dari area ROI
    MAX_DENSITY = 0.35        # Maksimal 35% (mencegah false positive dari stempel/teks padat)
    
    if fg_pixels >= MIN_FG_PIXELS and (MIN_DENSITY <= fg_density <= MAX_DENSITY) and len(valid_components) > 2:
        status = "SIGNATURE PRESENT"
    else:
        status = "SIGNATURE ABSENT"
        
    results = {
        "roi_name": roi_name,
        "total_pixels": total_pixels,
        "fg_pixels": fg_pixels,
        "fg_density": fg_density,
        "num_components": len(valid_components),
        "status": status,
        "images": {
            "Original ROI": roi,
            "Grayscale": gray,
            "Global Thresh": thresh_global,
            "Otsu Thresh": thresh_otsu,
            "Adaptive Thresh": thresh_adaptive,
            "Morphology Open": opened,
            "Morphology Close": closed,
            "Morphology Final": closed
        }
    }
    
    return results


def show_threshold_and_morphology(results, title, save_name):
    stage_order = [
        ("Original ROI", results["images"]["Original ROI"]),
        ("Grayscale", results["images"]["Grayscale"]),
        ("Global Thresh", results["images"]["Global Thresh"]),
        ("Otsu Thresh", results["images"]["Otsu Thresh"]),
        ("Adaptive Thresh", results["images"]["Adaptive Thresh"]),
        ("Opening", results["images"]["Morphology Open"]),
        ("Closing", results["images"]["Morphology Close"]),
        ("Morphology Final", results["images"]["Morphology Final"]),
    ]

    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    fig.suptitle(f"{title} - Thresholding & Morphological Operations", fontsize=14, fontweight='bold')

    for ax, (name, image) in zip(axes.flat, stage_order):
        if len(image.shape) == 3:
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            ax.imshow(rgb)
        else:
            ax.imshow(image, cmap='gray')
        ax.set_title(name)
        ax.axis('off')

    for ax in axes.flat[len(stage_order):]:
        ax.axis('off')

    plt.tight_layout()
    plt.savefig(save_name, dpi=200, bbox_inches='tight')
    plt.show()

# --- PENGUJIAN PADA CITRA ---
# Koordinat ROI dalam rasio (ymin, ymax, xmin, xmax)
# Area Dekan/Kepala Sekolah (Ada Tanda Tangan)
ROI_SIGNATURE = (0.13, 0.36, 0.62, 0.88)

# Area Kosong/Tanpa Tanda Tangan (Margin Atas)
ROI_NO_SIGNATURE = (0.02, 0.12, 0.20, 0.50)

# Uji pada semua citra dari 01 sampai 09
test_files = [
    ("01_HighQuality_Enhanced.jpg", "01 - High Quality"),
    ("02_LowContrast.jpg", "02 - Low Contrast"),
    ("03_Blurred.jpg", "03 - Blurred"),
    ("04_HighNoise.jpg", "04 - High Noise"),
    ("05_LowResolution_Upsampled.jpg", "05 - Low Resolution"),
    ("06_Faded_Underexposed.jpg", "06 - Faded/Underexposed"),
    ("07_ColorShift_WarmTint.jpg", "07 - Color Shift"),
    ("08_JPEGCompression_Artifacts.jpg", "08 - Compression Artifacts"),
    ("09_CombinedDegradation.jpg", "09 - Combined Degradation")
]

for file_name, desc in test_files:
    print(f"\n=================== UJI CITRA: {desc} ({file_name}) ===================")
    
    # Uji 1: Area Ada Tanda Tangan
    res_sig = process_signature_roi(file_name, ROI_SIGNATURE, roi_name="Area Dekan (Ada TTD)")
    if res_sig:
        print(f"[{res_sig['roi_name']}] -> Status: {res_sig['status']}")
        print(f"  - Foreground Pixels : {res_sig['fg_pixels']} / {res_sig['total_pixels']}")
        print(f"  - Kepadatan Piksel   : {res_sig['fg_density']:.4f}")
        print(f"  - Komponen Terhubung : {res_sig['num_components']}")
        show_threshold_and_morphology(
            res_sig,
            f"{desc} - Area Dekan",
            f"{file_name}_area_dekan_threshold_morphology.png"
        )

    # Uji 2: Area Tanpa Tanda Tangan
    res_nosig = process_signature_roi(file_name, ROI_NO_SIGNATURE, roi_name="Area Blank (Tanpa TTD)")
    if res_nosig:
        print(f"[{res_nosig['roi_name']}] -> Status: {res_nosig['status']}")
        print(f"  - Foreground Pixels : {res_nosig['fg_pixels']} / {res_nosig['total_pixels']}")
        print(f"  - Kepadatan Piksel   : {res_nosig['fg_density']:.4f}")
        print(f"  - Komponen Terhubung : {res_nosig['num_components']}")
        show_threshold_and_morphology(
            res_nosig,
            f"{desc} - Area Blank",
            f"{file_name}_area_blank_threshold_morphology.png"
        )