from collections import Counter
import math

def evaluate_clusters(clusters):
    """
    clusters: List of clusters, where each cluster is a list of elements.
              Each element is a tuple (id, label) where label is 'A' or 'B'.
    """
    total_items = 0
    correct_assignments = 0
    total_entropy = 0

    print("Cluster Evaluation Summary:\n")

    for i, cluster in enumerate(clusters):
        labels = [label for _, label in cluster]
        count = Counter(labels)
        total = len(labels)
        majority_label, majority_count = count.most_common(1)[0]

        # Entropy calculation
        entropy = 0
        for label_count in count.values():
            p = label_count / total
            entropy -= p * math.log2(p)

        print(f"Cluster {i + 1}:")
        print(f"  Total items: {total}")
        print(f"  Label counts: {dict(count)}")
        print(f"  Majority label: {majority_label} ({majority_count})")
        print(f"  Entropy: {entropy:.4f}\n")

        total_items += total
        correct_assignments += majority_count
        total_entropy += entropy * total  # Weighted by cluster size

    # Overall metrics
    purity = correct_assignments / total_items if total_items > 0 else 0
    avg_entropy = total_entropy / total_items if total_items > 0 else 0

    print(f"Overall Purity: {purity:.4f}")
    print(f"Weighted Average Entropy: {avg_entropy:.4f}")

# Example usage
# clusters = [
#     [(1, 'A'), (2, 'B'), (3, 'A')],  # Cluster 1: 2A, 1B
#     [(4, 'B'), (5, 'B')],            # Cluster 2: 2B
#     [(6, 'A'), (7, 'B'), (8, 'A')],  # Cluster 3: 2A, 1B
# ]

# clusters = [
#     # Cluster 1: 8 A, 5 B
#     [(1, 'A'), (2, 'A'), (3, 'A'), (4, 'A'), (5, 'A'), (6, 'A'), (7, 'A'), (8, 'A'),
#      (9, 'B'), (10, 'B'), (11, 'B'), (12, 'B'), (13, 'B')],
#     # Cluster 2: 4 A, 5 B
#     [(14, 'A'), (15, 'A'), (16, 'A'), (17, 'A'),
#      (18, 'B'), (19, 'B'), (20, 'B'), (21, 'B'), (22, 'B')],
#     # Cluster 3: 3 A, 4 B
#     [(23, 'A'), (24, 'A'), (25, 'A'),
#      (26, 'B'), (27, 'B'), (28, 'B'), (29, 'B')],
#     # Cluster 4: 3 A, 3 B
#     [(30, 'A'), (31, 'A'), (32, 'A'),
#      (33, 'B'), (34, 'B'), (35, 'B')],
# ]

# clusters = [
#     [(1, 'A'), (2, 'B'), (3, 'B')],
#     [(4, 'A'), (5, 'A'), (6, 'A'), (7, 'A'), (8, 'A'), (9, 'A'), (10, 'B'), (11, 'B')],
#     [(12, 'A'), (13, 'B')],
#     [(14, 'A'), (15, 'B'), (16, 'B'), (17, 'B'), (18, 'B')],
#     [(19, 'A'), (20, 'A'), (21, 'B')],
#     [(22, 'A'), (23, 'A'), (24, 'A'), (25, 'B'), (26, 'B'), (27, 'B')],
#     [(28, 'B')],
#     [(29, 'B')],
#     [(30, 'A'), (31, 'B')],
# ]

# clusters = [
#     [(1, 'A'), (2, 'B'), (3, 'B'), (4, 'B'), (5, 'B'), (6, 'B'), (7, 'B'), (8, 'B'), (9, 'B')],
#     [(10, 'A'), (11, 'A'), (12, 'A'), (13, 'A')],
#     [(14, 'A'), (15, 'A'), (16, 'A'), (17, 'A'), (18, 'B')],
#     [(19, 'B')],
#     [(20, 'A'), (21, 'A'), (22, 'A'), (23, 'A'), (24, 'B'), (25, 'B'), (26, 'B')],
#     [(27, 'A'), (28, 'A'), (29, 'B'), (30, 'B'), (31, 'B')],
# ]

# clusters = [
#     [(1, 'A'), (2, 'A'), (3, 'A'), (4, 'A'), (5, 'A'), (6, 'A'), (7, 'A'),
#      (8, 'B'), (9, 'B'), (10, 'B'), (11, 'B'), (12, 'B'), (13, 'B'), (14, 'B'), (15, 'B')],
#     [(16, 'A'), (17, 'A'), (18, 'A'), (19, 'B'), (20, 'B'), (21, 'B'), (22, 'B')],
#     [(23, 'A'), (24, 'A'), (25, 'A'), (26, 'B'), (27, 'B'), (28, 'B')],
#     [(29, 'B')],
# ]

clusters = [
    [(1, 'A'), (2, 'A'), (3, 'A'), (4, 'A'), (5, 'A'), (6, 'B'), (7, 'B')],
    [(8, 'A'), (9, 'A'), (10, 'A'), (11, 'B'), (12, 'B')],
    [(13, 'B'), (14, 'B'), (15, 'B')],
    [(16, 'A'), (17, 'A'), (18, 'B'), (19, 'B'), (20, 'B'), (21, 'B'), (22, 'B'), (23, 'B'), (24, 'B'), (25, 'B')],
    [(26, 'A'), (27, 'A'), (28, 'B')],
]

# clusters = [
#     [(1, 'A'), (2, 'A'), (3, 'A'), (4, 'A'), (5, 'B')],
#     [(6, 'A'), (7, 'A'), (8, 'B')],
#     [(9, 'B'), (10, 'B')],
#     [(11, 'B')],
#     [(12, 'B')],
# ]

evaluate_clusters(clusters)