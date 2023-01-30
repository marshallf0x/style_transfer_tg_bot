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

This is my bot https://t.me/pic_style_transfer_bot maybe it's deployed now on hetzner host, but I don't have money for GPU on cloud, so It will take lots of time to generate.
On my local host with GPU GTX1650 it takes only 1.5-3 minutes

### How is it working on sceenshots

There you can see Inline keyboard

![tg1](https://user-images.githubusercontent.com/123880677/215392555-4ed1150c-b87e-4c41-862c-2f4d15798cc3.png)

And there it disappered 'cause was started proccess of uploading images

![tg2](https://user-images.githubusercontent.com/123880677/215392642-e60b6156-5cb6-4b73-b5d8-ddc6e11a49eb.png)

Some tests:

![tg3](https://user-images.githubusercontent.com/123880677/215392643-4ec176a3-9459-4b79-be53-40268c34a705.png)
![tg4](https://user-images.githubusercontent.com/123880677/215392647-1678a6df-e6a1-40f5-a5ea-2bde87b43d1c.png)
![tg5](https://user-images.githubusercontent.com/123880677/215392650-eec7691b-097d-4a51-a46d-764dee0a96af.png)
![tg6](https://user-images.githubusercontent.com/123880677/215392651-068d23f6-43e9-4d47-84b1-4b425156f6cc.png)
![tg7](https://user-images.githubusercontent.com/123880677/215392639-80b0992f-1908-42b8-ac16-8db20f2efbcd.png)

You can try it yourself! 
