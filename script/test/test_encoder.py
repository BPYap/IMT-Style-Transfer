import os

from imt.encoder.fasttext import FTEncoder
from imt.encoder.glove import GloveEncoder
from imt.encoder.universal_sentence_encoder import USEEncoder
from imt.util.config import load_yaml_config


if __name__ == '__main__':
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    PRETRAINED_CONFIG_PATH = os.path.join(ROOT_PATH, "config/pretrained_paths.yml")

    yaml_config = load_yaml_config(PRETRAINED_CONFIG_PATH)
    fasttext_path = yaml_config['fasttext_model_path']
    glove_path = yaml_config['glove_model_path']
    use_path = yaml_config['use_model_path']

    sentences = [
        "How is the weather today?",
        "The weather is fine.",
        "Hello World!",
        "The quick brown fox jumps over the lazy dog.",
        "Hi"
        ]
    encoders = [FTEncoder(fasttext_path), GloveEncoder(glove_path), USEEncoder(use_path)]

    for i, sentence in enumerate(sentences):
        print("=" * 80)
        print("Sentence: {}\n".format(sentence))
        for encoder in encoders:
            print("Getting vector from {}...".format(encoder.name))
            vector = encoder.get_vector(sentence)
            print("Vector: [{}, ...]".format(", ".join(str(x) for x in vector[:3])))
            print("Vector dimensions: {}\n".format(len(vector)))

    for encoder in encoders:
        print("Getting vectors from {}...".format(encoder.name))
        vectors = encoder.get_vectors(sentences)
        print("[")
        for vector in vectors:
            print(" [{}, ...]".format(", ".join(str(x) for x in vector[:3])))
        print("]")
        print("Vectors dimensions: {}\n".format(vectors.shape))
