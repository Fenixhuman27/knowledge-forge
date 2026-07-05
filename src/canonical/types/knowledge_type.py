from enum import Enum


class KnowledgeType(str, Enum):
    CONVERSATION = "conversation"
    MESSAGE = "message"

    PERSON = "person"
    ORGANIZATION = "organization"

    PROJECT = "project"
    TASK = "task"
    GOAL = "goal"

    IDEA = "idea"
    CONCEPT = "concept"

    DECISION = "decision"
    QUESTION = "question"
    ANSWER = "answer"

    EVENT = "event"
    DOCUMENT = "document"

    RELATIONSHIP = "relationship"