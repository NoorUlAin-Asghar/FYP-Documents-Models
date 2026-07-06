import os
import nibabel as nib

# INPUT ROOT
input_root = r"D:\F25-156\ISLES24\train\derivatives"

# OUTPUT FOLDERS
output_images = r"D:\F25-156\ISLES24\processed\images"
output_masks = r"D:\F25-156\ISLES24\processed\masks"

os.makedirs(output_images, exist_ok=True)
os.makedirs(output_masks, exist_ok=True)

# Get all subject folders
subjects = sorted([s for s in os.listdir(input_root) if s.startswith("sub-stroke")])

print(f"Total subjects found: {len(subjects)}\n")

saved_count = 0
skipped_count = 0
missing_files = 0

for subject in subjects:
    ses_path = os.path.join(input_root, subject, "ses-02")

    if not os.path.exists(ses_path):
        print(f"Skipping {subject} (no ses-02)")
        skipped_count += 1
        continue

    files = os.listdir(ses_path)

    dwi_file = None
    mask_file = None

    for f in files:
        if "dwi.nii.gz" in f:
            dwi_file = f
        elif "lesion-msk.nii.gz" in f:
            mask_file = f

    if dwi_file is None or mask_file is None:
        print(f"Missing files in {subject}")
        missing_files += 1
        continue

    # Full paths
    dwi_path = os.path.join(ses_path, dwi_file)
    mask_path = os.path.join(ses_path, mask_file)

    try:
        # Load images
        dwi_img = nib.load(dwi_path)
        mask_img = nib.load(mask_path)

        # Convert names (.nii.gz → .nii)
        dwi_name = dwi_file.replace(".nii.gz", ".nii")
        mask_name = mask_file.replace(".nii.gz", ".nii")

        # Save uncompressed
        nib.save(dwi_img, os.path.join(output_images, dwi_name))
        nib.save(mask_img, os.path.join(output_masks, mask_name))

        print(f"Saved {subject}")
        saved_count += 1

    except Exception as e:
        print(f"Error processing {subject}: {e}")
        skipped_count += 1

# Final summary
print("\n===== SUMMARY =====")
print(f"Total subjects       : {len(subjects)}")
print(f"Successfully saved   : {saved_count}")
print(f"Missing files cases  : {missing_files}")
print(f"Other skipped cases  : {skipped_count}")
print("===================")