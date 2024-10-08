import pandas as pd



df = pd.read_csv('models.csv')

models = []
providers = []

for _, row in df.iterrows():
    if row['top_provider.max_completion_tokens'] > 0:
        max_completion_tokens = row['top_provider.max_completion_tokens']
    else:
        max_completion_tokens = 0
    #store model
    models.append([
        row['id'],    row['name'],    row['created'],    row['description'].replace("\n", ""),    row['context_length'],    row['per_request_limits'],    row['architecture.modality'],
        row['architecture.tokenizer'],    row['architecture.instruct_type'],    row['pricing.prompt'],    row['pricing.completion'],    row['pricing.image'],
        row['pricing.request'],    row['top_provider.context_length'],    max_completion_tokens,
        row['top_provider.is_moderated'],    row['preferred_provider'],    row['model_type'],
    ])

def list_all():
    """
    Display available models and providers.

    This function prints the available models and providers to the console.
    It helps users understand the options for model and provider selection.
    """
    print("\nmodels:\n")
    for model in models:
        print(f'["{model[0]}", "{model[1]}", {model[2]}, "{model[3]}", {model[4]}, "", "{model[6]}", "{model[7]}", "{model[8]}", {model[9]}, {model[10]}, {model[11]}, {model[12]}, {model[13]}, {model[14]}, {model[15]}, "{model[16]}", "{model[17]}", []],')



df = pd.read_csv('samples.csv')

voice_samples = {}

# Populate the voice_samples dictionary
for _, row in df.iterrows():
    voice_name = row['voice_name']
    voice_samples[voice_name] = row['url']

# Print some information to verify the data loading
print(f"Loaded data for {len(models)} models")
print(f"Loaded {len(voice_samples)} voice samples")

# Example of how to access the data (WIP):
# print(model_data['Meta: Llama 3.2 3B Instruct']['id'])
# print(model_data['Meta: Llama 3.2 3B Instruct']['context_length'])
# print(model_index['Meta: Llama 3.2 3B Instruct'])  # Get index of a model
# print(index_to_model[0])  # Get model name for index 0
