# Telegram Bot with style transfer

### Description
This is my finall DLS MIPT course project which I did using aiogram and torch GAN from there https://github.com/crowsonkb/style-transfer-pytorch


### Install
```sh
pip install -r requirements.txt
```
Also there I use my GPU and there is issue about torch wheel.

My cuda is 11.8 and I had to install unstable version, then it started use GPU and I did `pip freeze`:

```sh
pip uninstall torch
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu118
```

Check your command here https://pytorch.org/get-started/locally

Now it should works! If you're not able to use GPU - remove `--device cuda:0` from `bot.py`, line 91

### Tests
