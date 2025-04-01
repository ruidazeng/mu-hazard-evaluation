# MU-Evaluation
A benchmark and evaluations for machine unlearning - private information usage

## Reproduction Steps

```
python3 -m rmu.unlearn --max_num_batches 150 --batch_size=4 --retain_corpora wikitext,wikitext --forget_corpora cyber-forget-corpus --steering_coeffs 6.5,6.5 --alpha 1200,1200 --lr 5e-5 --seed 42 --output_dir models/zephyr_rmu --verbose
```

Then:

```
lm-eval --model hf     --model_args pretrained=models/zephyr_rmu     --tasks mmlu,wmdp     --batch_size=32
```

