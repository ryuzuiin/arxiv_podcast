import os
import azure.cognitiveservices.speech as speechsdk
from config.credentials import AZURE_TTS_KEY, AZURE_TTS_REGION

def synthesize_speech(text: str, filename: str):
    # 创建语音配置
    speech_config = speechsdk.SpeechConfig(
        subscription=AZURE_TTS_KEY,
        region=AZURE_TTS_REGION
    )

    # 选一个日语女声（可改为他人声线）
    speech_config.speech_synthesis_voice_name = "ja-JP-NanamiNeural"

    # 设置输出路径
    audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)

    # 创建合成器
    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=audio_config
    )

    # 合成
    result = synthesizer.speak_text_async(text).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"[TTS] 音声生成成功: {filename}")
    else:
        print(f"[TTS] 音声生成失敗: {result.reason}")
