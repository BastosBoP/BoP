# src/community_rewards.py

def evaluate_community(user, evaluation_details, points_per_evaluation=25):
    """
    Award points for evaluating a community aspect.
    
    :param user: The user performing the evaluation.
    :param evaluation_details: Details of the evaluation performed by the user.
    :param points_per_evaluation: The number of points awarded per evaluation.
    :return: A message indicating the points awarded.
    """
    # Simulate evaluating a community aspect
    points_awarded = points_per_evaluation
    return f"User {user} evaluated the community and earned {points_awarded} points."

def participate_in_discussion(user, discussion_topic, points_per_participation=15):
    """
    Award points for participating in a community discussion.
    
    :param user: The user participating in the discussion.
    :param discussion_topic: The topic of the discussion the user is participating in.
    :param points_per_participation: The number of points awarded per participation.
    :return: A message indicating the points awarded.
    """
    # Simulate participating in a community discussion
    points_awarded = points_per_participation
    return f"User {user} participated in the discussion on '{discussion_topic}' and earned {points_awarded} points."
