# AI Waste Detection

## Goal

The AI module identifies floating solid waste from images captured by the onboard camera.

## Pipeline

```text
Image
  ↓
Pre-processing
  ↓
YOLOv8
  ↓
Detection boxes
  ↓
Class + confidence
  ↓
Target selection
```

## Dataset

A project-specific dataset should contain images collected from realistic pond/lake conditions. Different lighting, viewing angles, distances, reflections and partially submerged objects should be represented.

## Training

The dataset can be labelled and used to train a YOLOv8 model. Training and validation results should be stored in the `models/` documentation when the final dataset is available.

## Deployment

The trained model is intended to run on the Raspberry Pi. Model size and inference speed should be considered along with detection accuracy.

## Honest reporting

Only measured metrics should be reported in the repository. Recommended metrics include precision, recall, mAP and inference FPS.
