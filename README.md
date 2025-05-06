## License and Usage

This project and all associated files are **proprietary** and are shared for demonstration purposes only. Redistribution, modification, or use of this model or code without explicit permission is strictly prohibited.

To request access or collaboration, please contact the author.

# Model 

 Lyrical Transformer: Fine-Tuning GPT-2 on Rhyming Structures in Rap


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


This project is **strictly educational**. It does not aim to replicate or impersonate any artist, nor is it affiliated with, endorsed by, or commercialized in relation to Eminem or his estate. The lyrics used were publicly available and not redistributed in dataset form. All outputs are experimental and intended solely to showcase LLM fine-tuning capabilities.


---


## Goals


* Demonstrate how **transformer-based LLMs** can learn non-traditional linguistic structures like **slant rhymes**, **internal rhymes**, and **phonetic approximations**.

* Explore how tokenization and attention mechanisms mirror the linguistic creativity found in high-level rap writing.

* Showcase a workflow for fine-tuning pre-trained models on domain-specific text using Hugging Face and Google Colab.


---


## Technical Stack


* Python (3.9+)

* [Hugging Face Transformers](https://github.com/huggingface/transformers)

* PyTorch

* Google Colab (for free GPU training)

* BeautifulSoup (for scraping)

* Custom tokenization and analysis scripts


---


## Sample Output


> *"Storage, porridge, orange in the corridor / Worded metaphors more distorted than ever before..."*

> *(Generated sample from fine-tuned GPT-2 model with rhyme seed prompt)*


---


## Ethical Note


As fans of hip-hop and NLP, we believe great artistry—like Eminem’s—is worth studying for its linguistic innovation. This project honors that by treating the lyrics as a case study in human creativity and machine learning, not as material for imitation or profit. If you have any questions or concerns, feel free to contact me at elsensoy@umich.edu.

<!-- Provide a longer summary of what this model is. -->

This is the model card of a transformers model that has been pushed on the Hub. 

- **Developed by:** Elida-Sensoy