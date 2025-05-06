
# Lyrical Transformer: Fine-Tuning GPT-2 on Rhyming Structures in Rap


## Project Overview


This project explores how large language models (LLMs), particularly transformers like GPT-2, can learn the rhyme density, multi-syllabic flow, and phonetic manipulation found in the lyrical style of complex hip-hop artists. The work was **inspired by an interview Eminem gave on 60 Minutes**, where he described how rhyming with "orange" is less about traditional rhyme rules and more about creatively **breaking down words into component sounds**—a process strikingly similar to how transformers operate on token sequences.


> “If you enunciate it and make it more than one syllable—like ‘or-ange’—you can rhyme it with door hinge, storage, or porridge.”

> — *Eminem, 60 Minutes interview*


This repository showcases the technical steps involved in:


* Scraping publicly available lyrics using Python.

* Preprocessing and tokenizing text for model consumption.

* Fine-tuning GPT-2 (`gpt2-medium`) on stylistically rich rap lyrics.

* Generating new lyrical content and analyzing phonetic/rhythmic patterns.

* Reflecting on how language models internalize rhyme, cadence, and lyrical style.

---

## Disclaimer 

>This project is **strictly educational**. It does not aim to replicate or impersonate any artist, nor is it affiliated with, endorsed by, or commercialized in relation to Eminem or his estate. The lyrics used were publicly available and not redistributed in dataset form. All outputs are experimental and intended solely to showcase LLM fine-tuning capabilities.

## Goals


* Demonstrate how **transformer-based LLMs** can learn non-traditional linguistic structures like **slant rhymes**, **internal rhymes**, and **phonetic approximations**.

* Explore how tokenization and attention mechanisms mirror the linguistic creativity found in high-level rap writing.

* Showcase a workflow for fine-tuning pre-trained models on domain-specific text using Hugging Face and Google Colab.

## Technical Stack

* Python (3.9+)

* [Hugging Face Transformers](https://github.com/huggingface/transformers)

* PyTorch

* Google Colab (for free GPU training)

* BeautifulSoup (for scraping)

* Custom tokenization and analysis scripts
---

## Sample Output 1:

> *(Prompt: "I ate three cupcakes". Generated sample from fine-tuned GPT-2 model with rhyme seed prompt)*
```Colab
 from transformers import pipeline, set_seed
 
 generator = pipeline("text-generation", model="Elida-Sensoy/gpt2-eminem-lyrics")
 set_seed(52)  # for reproducibility
 
 prompt = "I ate three cupcakes."  # starting line
 
 results = generator(
     prompt,
     max_length=200,
     num_return_sequences=3,      #  generate 3 completions
     temperature=1.75,             # higher = more creative
     top_p=0.95,                  #  nucleus sampling
     do_sample=True,
     truncation=True,
     pad_token_id=50256           # prevents warnings with GPT-2
 )
 
 for i, res in enumerate(results):
     print(f"\n🎵 Verse {i+1}:\n{res['generated_text']}")
```
> *🎵 Verse 1:
I ate three cupcakes but didn't get the fuckin' shit to drinkI've been goin' in deep, you need the "G" for me, so I said come get meThat shit ain't come with a rocket launcher in it itIt's an umbrella with a strap-onI said come, y'all gon' be fuckin' by in ten minutesI took it with both hands and used it to launchSpike your shoes and wear no underwear, now I don't fit in the storeOr maybe I should just run straight to the ERMy heart goes out to everybody, I'm 'bout to throw it awaySo stay clear my name 'fore you walk around with itI ain't smoking anything, just stay with the gist of itBut stay clear in my mind of why I am here tonightI know what you think'Cause at these funeral services, when it's rain[Chorus]There will always be a certain curse that will always befall a*

> *🎵 Verse 2:
I ate three cupcakes 'cause I was getting drunk Fuck the world 'cause I woke up with a brain tummy That's not my cause I'm not a fucking writer, I'm just an ass Fuck these things so damn hard I will just let these fags eat meAll they shit you say is shit because you don't give a fuck I did something a bit risky, changed the club too and went outThe way I sat it back and goof took off on your shit, fucked around with your equipment tooThey'd put a grenade in ya ass for fun Fuck it you fucked around a long time too Now you wanna blow up a flight from Toronto? I get up outta there You have one shot! Come and blow up a plane!No they ain't set at the start! They wanna know? They ain't ready when I shoot up that hotel ballroom full of gents!Fuck a fuckin' whore, I can fly away*

> *🎵 Verse 3:
I ate three cupcakes, then I heard they been taken awayI turned around and started going "Ha ha"Turned around and jumped back againGrabbed my camera in one hand and took a picture and I put it inside my heartJust to show you just how freaking insane my ex-wife (Maggie Ruess)Isn't that insane?Cause I don't need you being selfishAnd not even getting your respectBecause if there are things that you do that will benefit meEven the most basic necessities are necessitiesWhen a bitch who does not give a fuck, even comes up behindYou are selfishIf we did say somethin togetherThat if I went down in hell I might not be that personThere really should be some sort of warning sent outBut nobody wants to listenI need a father to hold me[Hook:]Pray I did something smart, so that when I passed life, it might not turnThis rhyme would be funny and be like "Yeah!"(Hmm)*

## Sample Output 2:

> *(Prompt: "There is no fun. Of course I am joking.". Generated sample from fine-tuned GPT-2 model with rhyme seed prompt)*
```Colab
 from transformers import pipeline, set_seed
 
 generator = pipeline("text-generation", model="Elida-Sensoy/gpt2-eminem-lyrics")
 set_seed(52)  # for reproducibility
 
 prompt = "There is no fun. Of course I am joking."  # starting line
 
 results = generator(
     prompt,
     max_length=200,
     num_return_sequences=3,      #  generate 3 completions
     temperature=1.75,             # higher = more creative
     top_p=0.95,                  #  nucleus sampling
     do_sample=True,
     truncation=True,
     pad_token_id=50256           # prevents warnings with GPT-2
 )
 
 for i, res in enumerate(results):
     print(f"\n🎵 Verse {i+1}:\n{res['generated_text']}")
```
     

Device set to use cpu

🎵 Verse 1:
There is no fun. Of course I am joking. But life's a game but your skill's on my line like no I don't know why so farI been in three lanes, never able to slow upThere's shit I do that will get me downThere's dirt, shit that's nastyBut there's nothing left.There's nothing that anybody gives a goddamn reason what there feels to feelThe only thing I love is competitionNow you know that feeling in which the greatest belongNobody ever caught it better than Nate Dworkin'You're still fucking beautifulNow take this chanceYou just wanna show them just how much you've already gotThere's shit you can do when you just liveIt only gets better when you put it in people's facesThat's called recognitionYou got recognition, DreThe fans can relate you just great if you act like meIf I did my jobs perfect rightYou can grow up to suck shit quicker.Yo I do everything in my power to bring it up

🎵 Verse 2:
There is no fun. Of course I am joking.So what's the problem?It's nothing, just the past that we liveThe future we plan for just don't arrive atAll we want is one for the time beingSo goodbye!You know we love ya!And if your home of horrorsA place where none existAnd I just can't say for certain thatThere isn't anyone out there who knowsThat I believe in loveMaybe that hurts (haha), maybe that's what hurtsMaybe it's the same maybe that made her sickThis monster loves me even though she's got me seething(whoa what?)[Chorus][Eminem (Sia): "Can't hear her sobbing louder anymore":]There comes a time in every couple that we settle or close or where our love or at this late dateIf we ever hit up that exact same placeOr get into an argument and I feel the need to kick it and call or text and reach

🎵 Verse 3:
There is no fun. Of course I am joking. You'd think there was more drama but there isn't.Don't even get me started..You're nuts. Go after 'em all!You feel so empty inside. Don't you ever breathe easy and hard again?This is all you ever talk. No! Stop. This is all you ever tell me that I must take!Now what we in this business do when we get heated..You can call me cold or sweet or bitter,Whatever our taste and your intentionsWe as Americans are always looking at each other and there won't be no difference we made in this competition, no difference.Canadians know that in each season we push off (off)The more changes make we endure in realityThen our relationship in the game (introduce us)...And so how are we set upon?Shoulders or nocksAre always pointed (a nose or a hump is placed in)We will tell you the difference is the bigger


---
## Ethical Note

---

## Ethical Considerations and Content Disclaimer

This project aims to study linguistic innovation and the capabilities of language models by analyzing complex lyrical structures, inspired by artists like Eminem. Such artistry is worth studying for its technical merit and creativity. This project honors that intent by treating the source material as a case study, not as material for imitation, impersonation, or profit.

**Content Warning:** The training data used (Eminem's publicly available lyrics) contains explicit language, slang, potentially offensive themes, and controversial content reflecting the artist's style and subject matter. Consequently, the generated output from this fine-tuned model is **not filtered** for potentially offensive, explicit, or unethical content. Generations may reflect the biases and language present in the training data. **Users should be aware of this potential output when interacting with the model.**

For details on usage rights and restrictions for the code and model itself, please refer to the `LICENSE` file. If you have any ethical concerns about this project, please contact the author at elsensoy@umich.edu.

- **Developed by:** Elida-Sensoy
