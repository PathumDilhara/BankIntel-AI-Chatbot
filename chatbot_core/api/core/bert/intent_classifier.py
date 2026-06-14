from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from dotenv import load_dotenv
import os
import torch.nn.functional as F
import json

load_dotenv()

tokenizer_path = os.getenv("bert_tokenizer_path")
model_path = os.getenv("bert_model_path")

with open('utils/label_map.json', 'r') as f:
    label_map = json.load(f)

class BERTIntentClassifer:
    def __init__(self):
        self.tokenizer= AutoTokenizer.from_pretrained(
            tokenizer_path,
        )

        self.model= AutoModelForSequenceClassification.from_pretrained(
            model_path,
            low_cpu_mem_usage=True
        )

        self.model.eval()

    def predict(self, msg:str):

        # Generating token ids for eahc word in msg with padding
        inputs = self.tokenizer(
            msg, 
            return_tensors='pt', 
            truncation=True, 
            padding=True,
        )

        # Model created logits values for above msg
        with torch.no_grad():
            outputs= self.model(**inputs)

        # outpouts contains loss=None, logits=Tensor, hidden_states=None, attentions=
        # let access logits
        logits= outputs.logits

        # convert logits into porbabilities
        probs = F.softmax(logits, dim=1)

        predicted_class = torch.argmax(probs, dim=1).item()
        
        confidence= torch.max(probs).item()

        return {
            'intent': label_map[str(predicted_class)],
            "confidence": confidence
        }
