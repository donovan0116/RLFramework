from abc import ABC, abstractmethod


class AgentBase(ABC):
    """
    智能体基类，定义了强化学习智能体的基本接口。
    """

    def __init__(self):
        pass

    @abstractmethod
    def select_action(self, state):
        """
        根据当前状态选择动作。
        :param state: 当前环境的状态
        :return: 选择的动作
        """
        pass

    @abstractmethod
    def learn(self, experience):
        """
        根据经验进行学习，更新智能体的参数。
        :param experience: 包含(state, action, reward, next_state, done)的元组
        """
        pass

    def save_model(self, filepath):
        """
        保存智能体的模型参数。
        :param filepath: 保存模型的路径
        """
        pass

    def load_model(self, filepath):
        """
        加载智能体的模型参数。
        :param filepath: 模型文件的路径
        """
        pass
