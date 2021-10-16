# import gym
# from gym import wrappers

# env = gym.make("MountainCar-v0")
# env = wrappers.Monitor(env, "/tmp/MountainCar-v0")

# for episode in range(2):
#     observation = env.reset()
#     step = 0
#     total_reward = 0

#     while True:
#         step += 1
#         env.render()
#         action = env.action_space.sample()
#         observation, reward, done, info = env.step(action)
#         total_reward += reward
#         if done:
#             print("Episode: {0},\tSteps: {1},\tscore: {2}"
#                   .format(episode, step, total_reward)
#             )
#             break
# env.close()

# # 1. It renders instances for 500 timesteps, performing random actions.
# import gym
# env = gym.make('Acrobot-v1')
# env.reset()
# for _ in range(500):
#     env.render()
#     env.step(env.action_space.sample())
# 2. To check all env available, uninstalled ones are also shown.
from gym import envs 
print(envs.registry.all())


# import gym
# env = gym.make('MountainCar-v0')

# env.reset()
# for _ in range(500):
#     env.render()
#     env.step(env.action_space.sample())