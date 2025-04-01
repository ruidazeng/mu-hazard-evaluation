# Machine Unlearning Hazard Evaluation

## WMDP
The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning by Li, Nathaniel, et al. Proceedings of the 41st International Conference on Machine Learning (ICML). 2024.

<img width="647" alt="Image" src="https://github.com/user-attachments/assets/b2311345-6921-46ea-8dd1-1edf5e109743" />

Paper: https://arxiv.org/abs/2403.03218
Site: https://www.wmdp.ai/
GitHub: https://github.com/centerforaisafety/wmdp?tab=readme-ov-file
Hugging Faces: https://huggingface.co/datasets/cais/wmdp

<img width="641" alt="Image" src="https://github.com/user-attachments/assets/ac09cca0-d820-40c9-968f-ee94e9771d2b" />

## Reproduction Steps

```
python3 -m rmu.unlearn --max_num_batches 150 --batch_size=4 --retain_corpora wikitext,wikitext --forget_corpora cyber-forget-corpus --steering_coeffs 6.5,6.5 --alpha 1200,1200 --lr 5e-5 --seed 42 --output_dir models/zephyr_rmu --verbose
```

Then:

```
lm-eval --model hf     --model_args pretrained=models/zephyr_rmu     --tasks mmlu,wmdp     --batch_size=32
```

## Results
![image](https://github.com/user-attachments/assets/6e855ac5-d5ab-4300-881d-3e8941374579)
