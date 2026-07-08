# PrivaFed: A Privacy-Preserving Federated Learning Framework

PrivaFed is a Privacy-Preserving Federated Learning (FL) Framework developed for automatic brain stroke lesion segmentation from MRI scans. The framework enables multiple institutions to collaboratively train deep learning segmentation models without sharing patient data, thereby preserving privacy while improving model generalization.

This repository contains the complete implementation, experiments, documentation, and supplementary resources used throughout our Final Year Project (FYP).

---

## Features

- Privacy-Preserving Federated Learning framework
- Centralized and Federated training pipelines
- Multiple state-of-the-art medical image segmentation models
- Support for heterogeneous and non-IID datasets
- Lightweight federated aggregation
- Transfer Learning (TL) experiments
- Complete preprocessing scripts
- Experiment logs and documentation

---

# Repository Structure

```
PrivaFed/
│
├── Additional Code/
│   ├── Dataset extraction scripts
│   ├── Dataset splitting utilities
│   ├── MRI preprocessing scripts
│   └── Helper utilities
│
├── Documents/
│   ├── Final Year Project Report
│   ├── Experiment & Result Sheets
│   └── Project Presentations
│
├── Literature Review/
│   └── Research papers studied during the project
│
├── Models/
│   ├── ISLES22/
│   │   ├── Centralized Learning
│   │   └── Federated Learning
│   │
│   ├── ISLES24/
│   │   ├── Centralized Learning
│   │   └── Federated Learning
│   │
│   ├── Combined/
│   │   └── Non-IID Federated Learning experiments
│   │
│   ├── Lightweight/
│   │   ├── ISLES22
│   │   ├── ISLES24
│   │   └── Combined
│   │
│   └── Transfer Learning/
│       ├── SegResNet
│       └── Lightweight SegResNet
│
└── README.md
```

---

# Directory Description

## Additional Code

This directory contains utility scripts that support the complete experimental pipeline.

Contents include:

- Dataset extraction from downloaded ISLES datasets
- Dataset splitting for centralized and federated setups
- MRI preprocessing
- Image resizing and normalization
- Helper scripts used during experimentation

---

## Documents

This directory contains all project documentation including:

- Final Year Project Report
- Experiment & Result Sheets
- Presentation Slides
- Project Documentation

---

## Models

This directory contains all implementations and experiments performed during this research.

The experiments are organized according to dataset and experimental setup.

### ISLES'22

Contains both

- Centralized Learning (CL)
- Federated Learning (FL)

experiments performed on the ISLES'22 dataset.

---

### ISLES'24

Contains both

- Centralized Learning (CL)
- Federated Learning (FL)

experiments performed on the ISLES'24 dataset.

---

### Combined

Contains heterogeneous and non-IID Federated Learning experiments where both ISLES'22 and ISLES'24 datasets are used simultaneously.

---

### Lightweight

Contains communication-efficient Federated Learning experiments where only the encoder and bottleneck layers of model (SegResNet) are aggregated.

Experiments include

- ISLES'22
- ISLES'24
- Combined Dataset

---

### Transfer Learning

Contains Transfer Learning experiments using pretrained SegResNet models.

Experiments include

- Standard SegResNet
- Lightweight SegResNet

---

## Literature Review

Contains research papers, surveys, and publications that were studied throughout the research phase of this project.

These papers helped in selecting suitable segmentation models, federated learning algorithms, and privacy-preserving techniques.

---

# Dataset

This project utilizes publicly available brain stroke MRI datasets.

- **ISLES'22**
  - 250 Diffusion Weighted MRI (DWI) scans with lesion masks

- **ISLES'24**
  - 149 Diffusion Weighted MRI (DWI) scans with lesion masks

---

# Data Preprocessing

Since the ISLES datasets are already partially preprocessed, only minimal preprocessing was required.

The preprocessing pipeline includes:

- Intensity normalization
- MRI volume resizing
- Spatial resampling
- Standardized voxel dimensions
- Tensor generation for model training

Input resolutions used during experiments:

| Experiment | Resolution |
|------------|------------|
| ISLES'22 | 96 × 96 × 96 |
| ISLES'24 | 128 × 128 × 128 |
| Combined | 192 × 192 × 192 |

---

# Experimental Setups

## 1. ISLES'22 Centralized Learning

### Dataset

- 250 MRI scans

### Data Split

- Training: 80%
- Validation: 20%

### Training

- 50 epochs for all models except nnUNet
- nnUNet trained using 5-fold Cross Validation (20 epochs per fold)

### Models Evaluated

- Swin Factorizer
- Swin UNETR
- nnUNet
- SegResNet
- 3D UNet
- 2D UNet
- 2D ResUNet
- ResNet34
- ResNet50

### Best Performing Model

| Model | Validation DSC |
|--------|---------------|
| **nnUNet** | **0.7609** |

---

## 2. ISLES'24 Centralized Learning

### Dataset

149 MRI scans

### Data Split

| Training | Validation | Testing |
|----------|------------|---------|
|95        |24          |30       |

### Training

50 epochs

### Models Evaluated

- SegResNet
- Swin UNETR

### Best Performing Model

| Model         | Test DSC   |
|---------------|------------|
| **SegResNet** | **0.6384** |

---

## 3. ISLES'22 Federated Learning

### Clients

3

### Client Distribution

50 training samples per client

### Validation Set

50 samples

### Test Set

50 samples

### Communication Rounds

10

### Local Epochs

20

### Models Evaluated

- Swin Factorizer
- Swin UNETR
- SegResNet
- 3D UNet

### Aggregation Algorithms

- FedAvg
- FedProx
- FedAdam
- Scaffold

### Best Configuration

| Model         | Aggregation | Test DSC   |
|---------------|-------------|------------|
| **SegResNet** | **FedProx** | **0.7196** |

---

## 4. ISLES'24 Federated Learning

### Clients

2

### Client Distribution

50 training samples each

### Validation Set

20 samples

### Test Set

29 samples

### Communication Rounds

10

### Local Epochs

20

### Models Evaluated

- SegResNet
- Swin UNETR
- Swin Factorizer
- 3D UNet

### Aggregation Algorithms

- FedAvg
- FedProx

### Best Configuration

| Model         | Aggregation | Test DSC   |
|---------------|-------------|------------|
| **SegResNet** | **FedAvg**  | **0.7106** |

---

## 5. Combined Federated Learning (Non-IID)

The combined experiment evaluates PrivaFed under heterogeneous and non-IID conditions.

### Client Distribution

| Client   | Dataset              |
|----------|----------------------|
| Client 0 | 100 ISLES'24 samples |
| Client 1 | 75 ISLES'22 samples  |
| Client 2 | 75 ISLES'22 samples  |

### Validation

- ISLES'22: 50 samples
- ISLES'24: 24 samples

### Testing

- ISLES'22: 50 samples
- ISLES'24: 25 samples

### Communication Rounds

10

### Local Epochs

20

### Personalization

After global aggregation, the best global model is redistributed to all clients, where each client performs an additional **5 local epochs** for personalized adaptation.

### Model

- SegResNet

### Aggregation Algorithms

- FedAvg
- FedProx

### Best Configuration

| Aggregation | Best Global Test DSC |
|-------------|----------------------|
| **FedAvg**  | **0.6842**           |

---

## 6. Lightweight Federated Learning

To reduce communication overhead, only the encoder and bottleneck layers of SegResNet are shared between clients and the server.

### Model

- SegResNet

### Aggregation

- FedProx

### Communication Reduction

- Full Model Parameters: **4,700,897**
- Lightweight Parameters: **4,399,344**
- Communication Reduction: **6.41%**

Experiments were conducted on:

- ISLES'22
- ISLES'24
- Combined Dataset

---

## 7. Transfer Learning

Transfer Learning experiments pretrained SegResNet on ISLES'22 before fine-tuning on ISLES'24.

### Pretraining Dataset

ISLES'22

### Fine-tuning Dataset

ISLES'24

### Model

SegResNet

### Aggregation

FedProx

### Best Results

| Experiment                      | Test DSC   |
|---------------------------------|------------|
| Transfer Learning               | **0.7064** |
| Transfer Learning + Lightweight | **0.7017** |

---

# Models Used

- SegResNet
- Swin UNETR
- Swin Factorizer
- nnUNet
- 3D UNet
- 2D UNet
- 2D ResUNet
- ResNet34
- ResNet50

---

# Federated Aggregation Algorithms

The following federated optimization algorithms were evaluated:

| Algorithm    | Description                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------|
| **FedAvg**   | Standard federated averaging algorithm that aggregates client model weights.                  |
| **FedProx**  | Extends FedAvg with a proximal regularization term to improve training on heterogeneous data. |
| **FedAdam**  | Adaptive server-side optimization using the Adam optimizer.                                   |
| **Scaffold** | Reduces client drift using control variates for more stable federated optimization.           |

---

# Future Work

Possible future improvements include:

- Differential Privacy integration
- Secure Aggregation protocols
- Cross-silo deployment
- Multi-modal MRI segmentation
- Multi-institution clinical validation
- Communication compression techniques

---

# Citation

If you use this repository in your research, please cite our Final Year Project.

```
@misc{PrivaFed2026,
  title={PrivaFed: Privacy-Preserving Federated Learning for Brain Stroke Segmentation},
  author={Final Year Project Team},
  year={2026}
}
```

---

# License

This repository is intended for academic and research purposes. It is licensed under MIT License.
