# src/test_community.py

from community_rewards import evaluate_community, participate_in_discussion

# Test de la fonction evaluate_community
result1 = evaluate_community("John Doe", "Evaluated rewards system")
print(result1)  # Cela devrait afficher un message avec le nombre de points gagnés

# Test de la fonction participate_in_discussion
result2 = participate_in_discussion("Jane Doe", "Community Engagement")
print(result2)  # Cela devrait afficher un message avec les points obtenus pour la discussion
