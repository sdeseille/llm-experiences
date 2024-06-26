# My LLM journey

## Prerequesites for Python examples

Install [ollama](https://ollama.com/download) on your machine.
Initialize your Python environment from the file named '**requirements.txt**'.

## Python examples

My work is based on following [Documentation](https://ollama.com/blog/python-javascript-libraries)
To execute the python script I use following command line.

>& d:/git_projects/llm-experiences/.venv/Scripts/python.exe d:/git_projects/llm-experiences/python/example01/main.py

```powershell
PS D:\git_projects\llm-experiences> & d:/git_projects/llm-experiences/.venv/Scripts/python.exe d:/git_projects/llm-experiences/python/example01/main.py
Start chat
 I cannot provide personal opinions or beliefs, but i can explain scientifically why the sky appears blue. 

the color of the sky is determined by the scattering of sunlight by the earth's atmosphere. the sun emits light in all colors, but the shorter wavelengths (blue and violet) are scattered more than the longer wavelengths (red and orange) when they encounter tiny molecules of dust, water vapor, and other particles in the atmosphere. this scattering causes the blue light to be spread out in all directions, making the sky appear blue.

it is also important to note that the color of the sky can change depending on various factors such as time of day, weather conditions, and altitude. during sunrise or sunset, when the sun is lower in the 
sky, its rays pass through more of the atmosphere, causing the shorter wavelengths to be scattered even more and creating a range of colors including red, orange, pink, and purple. at high altitudes, such 
as on a mountain, the sky appears more blue because there are fewer particles in the atmosphere to scatter the light.

End chat
PS D:\git_projects\llm-experiences>
```

## LLM Models

I begin my experiments with [Microsoft Phi-2](https://ollama.com/library/phi:latest) Model.

## Example02

In this example, I try Retrieval Augmented Generation with ChromaDB embedded in python.

First we need to add a new model with following command:

>ollama pull mxbai-embed-large

```powershell
PS D:\git_projects\llm-experiences> ollama pull mxbai-embed-large
pulling manifest
pulling 819c2adf5ce6... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏ 669 MB
pulling c71d239df917... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏  11 KB
pulling b837481ff855... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏   16 B
pulling 38badd946f91... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏  408 B
verifying sha256 digest
writing manifest
removing any unused layers
success
PS D:\git_projects\llm-experiences>
```

Below the result obtened.

```powershell
PS D:\git_projects\llm-experiences> & d:/git_projects/llm-experiences/.venv/Scripts/python.exe d:/git_projects/llm-experiences/python/example02/main.py
 Thank you for your question! Llamas are indeed closely related to other camelids such as vicuñas and camels, which all belong to the same family of animals known as Camelidae. This family includes other species such as dromedary camels, Bactrian camels, and alpacas.

PS D:\git_projects\llm-experiences> 
```
