# Warm-up Kit for Erasing Invisible Competition @ NeurIPS 2024

This warm-up kit provides an exmaple of the evaluation process in the erasing invisible competition @ NeurIPS 2024.
Please note that the evaluation setup and metrics here are examples and are not exactly the same as the setups used in the competition.

### Setup
1. Download models from the release page and put in `./models` folder.
2. Install with `pip install -e .`

### Attack
Download images from dropbox (link) and attack them with your methods.

### Evaluate
Evaluate with `erasinginvisible --path <attacked_image_path> --orgpath <orginal_image_path>`