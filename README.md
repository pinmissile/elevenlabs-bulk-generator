# elevenlabs-bulk-generator
Quick and dirty Python script for bulk synthesizing Elevenlabs voicelines

## Usage

Add your `API_KEY` and `VOICE_ID` to the config file.

`echo -e "API_KEY={YOUR_API_KEY_HERE}\rVOICE_ID={YOUR_VOICE_ID_HERE}" > ./config.py`

Make a `lines.txt` file in project root dir with the lines to generate. Use the following format, with a `\t` to delimit line from file name. 

```
I'm a cool voiceline!\tVOICE_LINE_1
I'm also a cool voiceline!\tVOICE_LINE_2
```

Run script with `python3 covnerter.py`
