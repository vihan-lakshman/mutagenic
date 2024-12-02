from huggingface_hub import login
from esm.models.esm3 import ESM3
from esm.sdk.api import ESM3InferenceClient, ESMProtein, GenerationConfig
import numpy as np

login()

model: ESM3InferenceClient = ESM3.from_pretrained("esm3-open").to("cpu") # or "cuda"
prompt = "RIL___HA"
esm_protein = ESMProtein(sequence=prompt)
protein = model.generate(esm_protein, GenerationConfig(track="sequence", temperature=0.7))

def get_random_mask_indices(protein, num_mask_residues=1):
    print('***')
    print(type(protein))
    sequence = protein.sequence
    mask_indices = np.random.choice(len(sequence), num_mask_residues)
    print(mask_indices)
    return mask_indices


print(get_random_mask_indices(protein))
