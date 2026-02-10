import numpy as np
import pickle
import os

OUTPUT_PATH = "model/artifacts/model.pkl"

def generate_synthetic_data(num_users=100, num_items=50, interactions=1000):
    data = []
    for _ in range(interactions):
        user = np.random.randint(0, num_users)
        item = np.random.randint(0, num_items)
        data.append((user, item))
    return data


def train_embeddings(data, num_users=100, num_items=50, dim=16):
    user_emb = np.random.normal(size=(num_users, dim))
    item_emb = np.random.normal(size=(num_items, dim))

    for user, item in data:
        user_emb[user] += item_emb[item] * 0.01
        item_emb[item] += user_emb[user] * 0.01

    return user_emb, item_emb


def main():
    os.makedirs("model/artifacts", exist_ok=True)

    data = generate_synthetic_data()
    user_emb, item_emb = train_embeddings(data)

    model = {
        "user_embeddings": user_emb,
        "item_embeddings": item_emb
    }

    with open(OUTPUT_PATH, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
