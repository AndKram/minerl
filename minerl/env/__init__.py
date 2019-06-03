# ------------------------------------------------------------------------------------------------
# Copyright (c) 2018 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------
import os

# import gym
# Perform the registration.
from gym.envs.registration import register
from minerl.env.spaces import Enum
from minerl.env.core import MineRLEnv, missions_dir

import numpy as np

import gym.spaces
  
register(
    id='MineRLTreechop-v0',
    entry_point='minerl.env:MineRLEnv',
    kwargs={
        'xml': os.path.join(missions_dir, 'treechop.xml'),
        'observation_space': gym.spaces.Dict({
            'pov': gym.spaces.Box(low=0, high=255, shape=(64,64,3), dtype=np.uint8),
            # 'XPos': gym.spaces.Box(low=-100000, high=100000, shape=(1,), dtype=np.int32),
            # 'ZPos': gym.spaces.Box(low=-100000, high=100000, shape=(1,), dtype=np.int32)
        }),
        'action_space': gym.spaces.Dict({
            "forward": gym.spaces.Discrete(2), 
            "back": gym.spaces.Discrete(2), 
            "left": gym.spaces.Discrete(2), 
            "right": gym.spaces.Discrete(2), 
            "jump": gym.spaces.Discrete(2), 
            "sneak": gym.spaces.Discrete(2), 
            "sprint": gym.spaces.Discrete(2), 
            "attack": gym.spaces.Discrete(2),
            "camera": gym.spaces.Box(low=-180, high=180, shape=(2,), dtype=np.float32),
        }),
    },
    max_episode_steps=8000,
    reward_threshold=64.0,
)



#######################
## NAVIGATE
#######################

register(
    id='MineRLNavigate-v0',
    entry_point='minerl.env:MineRLEnv',
    kwargs={
        'xml': os.path.join(missions_dir, 'navigation.xml'),
        'observation_space': gym.spaces.Dict({
            'pov': gym.spaces.Box(low=0, high=255, shape=(64, 64, 3), dtype=np.uint8),
            'inventory': gym.spaces.Dict({
                'dirt': gym.spaces.Box(low=0, high=2304, shape=(1,), dtype=np.int)
            }),
            'compassAngle': gym.spaces.Box(low=-180.0, high=180.0, shape=(1,), dtype=np.float32)
        }),
        'action_space': gym.spaces.Dict({
            "forward": gym.spaces.Discrete(2),
            "back": gym.spaces.Discrete(2),
            "left": gym.spaces.Discrete(2),
            "right": gym.spaces.Discrete(2),
            "jump": gym.spaces.Discrete(2),
            "sneak": gym.spaces.Discrete(2),
            "sprint": gym.spaces.Discrete(2),
            "attack": gym.spaces.Discrete(2),
            "camera": gym.spaces.Box(low=-180, high=180, shape=(2,), dtype=np.float32),
            "place": spaces.Enum('none', 'dirt')
        }),
    },
    max_episode_steps=6000,
)

register(
    id='MineRLNavigateDense-v0',
    entry_point='minerl.env:MineRLEnv',
    kwargs={
        'xml': os.path.join(missions_dir, 'navigationDense.xml'),
        'observation_space': gym.spaces.Dict({
            'pov': gym.spaces.Box(low=0, high=255, shape=(64, 64, 3), dtype=np.uint8),
            'inventory': gym.spaces.Dict({
                'dirt': gym.spaces.Box(low=0, high=2304, shape=(1,), dtype=np.int)
            }),
            'compassAngle': gym.spaces.Box(low=-180.0, high=180.0, shape=(1,), dtype=np.float32)
        }),
        'action_space': gym.spaces.Dict({
            "forward": gym.spaces.Discrete(2), 
            "back": gym.spaces.Discrete(2), 
            "left": gym.spaces.Discrete(2), 
            "right": gym.spaces.Discrete(2), 
            "jump": gym.spaces.Discrete(2), 
            "sneak": gym.spaces.Discrete(2), 
            "sprint": gym.spaces.Discrete(2), 
            "attack": gym.spaces.Discrete(2),
            "camera": gym.spaces.Box(low=-180, high=180, shape=(2,), dtype=np.float32),  # Pitch, Yaw
            "place": spaces.Enum('none', 'dirt')
        })
    },
    max_episode_steps=6000,
)


register(
    id='MineRLNavigateExtreme-v0',
    entry_point='minerl.env:MineRLEnv',
    kwargs={
        'xml': os.path.join(missions_dir, 'navigationExtreme.xml'),
        'observation_space': gym.spaces.Dict({
            'pov': gym.spaces.Box(low=0, high=255, shape=(64, 64, 3), dtype=np.uint8),
            'inventory': gym.spaces.Dict({
                'dirt': gym.spaces.Box(low=0, high=2304, shape=(1,), dtype=np.int)
            }),
            'compassAngle': gym.spaces.Box(low=-180.0, high=180.0, shape=(1,), dtype=np.float32)
        }),
        'action_space': gym.spaces.Dict({
            "forward": gym.spaces.Discrete(2),
            "back": gym.spaces.Discrete(2),
            "left": gym.spaces.Discrete(2),
            "right": gym.spaces.Discrete(2),
            "jump": gym.spaces.Discrete(2),
            "sneak": gym.spaces.Discrete(2),
            "sprint": gym.spaces.Discrete(2),
            "attack" : gym.spaces.Discrete(2),
            "camera": gym.spaces.Box(low=-180, high=180, shape=(2,), dtype=np.float32),
            "place": spaces.Enum('none', 'dirt')
        }),
    },
    max_episode_steps=6000,
)

register(
    id='MineRLNavigateExtremeDense-v0',
    entry_point='minerl.env:MineRLEnv',
    kwargs={
        'xml': os.path.join(missions_dir, 'navigationExtremeDense.xml'),
        'observation_space': gym.spaces.Dict({
            'pov': gym.spaces.Box(low=0, high=255, shape=(64, 64, 3), dtype=np.uint8),
            'inventory': gym.spaces.Dict({
                'dirt': gym.spaces.Box(low=0, high=2304, shape=(1,), dtype=np.int)
            }),
            'compassAngle': gym.spaces.Box(low=-180.0, high=180.0, shape=(1,), dtype=np.float32)
        }),
        'action_space': gym.spaces.Dict({
            "forward": gym.spaces.Discrete(2),
            "back": gym.spaces.Discrete(2),
            "left": gym.spaces.Discrete(2),
            "right": gym.spaces.Discrete(2),
            "jump": gym.spaces.Discrete(2),
            "sneak": gym.spaces.Discrete(2),
            "sprint": gym.spaces.Discrete(2),
            "attack": gym.spaces.Discrete(2),
            "camera": gym.spaces.Box(low=-180, high=180, shape=(2,), dtype=np.float32),  # Pitch, Yaw
            "place": spaces.Enum('none', 'dirt')
        })
    },
    max_episode_steps=6000,
)


#######################
#     Obtain Iron     #
#######################
register(
    id='MineRLObtainIronPickaxe-v0',
    entry_point='minerl.env:MineRLEnv',
    kwargs={
        'xml': os.path.join(missions_dir, 'obtainIronPickaxe.xml'),
        'observation_space': gym.spaces.Dict({
            'pov': gym.spaces.Box(low=0, high=255, shape=(64, 64, 3), dtype=np.uint8),
            'inventory': gym.spaces.Dict({
                'dirt': gym.spaces.Box(low=0, high=2304, shape=(1,), dtype=np.int),
                'coal': gym.spaces.Box(low=0, high=2304, shape=(1,), dtype=np.int),
                'torch': gym.spaces.Box(low=0, high=2304, shape=(1,), dtype=np.int),
                'log': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'planks': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'stick': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'crafting_table': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'wooden_pickaxe': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'stone': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'furnace': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'stone_pickaxe': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'iron_ore': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'iron_ingot': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'iron_pickaxe': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
            }),
        }),
        'action_space': gym.spaces.Dict({
            "forward": gym.spaces.Discrete(2),
            "back": gym.spaces.Discrete(2),
            "left": gym.spaces.Discrete(2),
            "right": gym.spaces.Discrete(2),
            "jump": gym.spaces.Discrete(2),
            "sneak": gym.spaces.Discrete(2),
            "sprint": gym.spaces.Discrete(2),
            "attack": gym.spaces.Discrete(2),
            "camera": gym.spaces.Box(low=-180, high=180, shape=(2,), dtype=np.float32),  # Pitch, Yaw
            "place": spaces.Enum('none', 'dirt', 'stone', 'crafting_table', 'furnace', 'torch'),
            "craft": spaces.Enum('none', 'torch', 'stick', 'planks'),
            "nearbyCraft": spaces.Enum('none', 'wooden_axe', 'wooden_pickaxe', 'stone_axe', 'stone_pickaxe',
                                       'iron_pickaxe', 'crafting_table', 'furnace'),
            "nearbySmelt": spaces.Enum('none', 'iron_ingot', 'coal')
        })
    },
    max_episode_steps=6000,
)


#######################
#   Obtain Diamond    #
#######################
register(
    id='MineRLObtainDiamond-v0',
    entry_point='minerl.env:MineRLEnv',
    kwargs={
        'xml': os.path.join(missions_dir, 'obtainIronPickaxe.xml'),
        'observation_space': gym.spaces.Dict({
            'pov': gym.spaces.Box(low=0, high=255, shape=(64, 64, 3), dtype=np.uint8),
            'inventory': gym.spaces.Dict({
                'dirt': gym.spaces.Box(low=0, high=2304, shape=(1,), dtype=np.int),
                'coal': gym.spaces.Box(low=0, high=2304, shape=(1,), dtype=np.int),
                'torch': gym.spaces.Box(low=0, high=2304, shape=(1,), dtype=np.int),
                'log': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'planks': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'stick': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'crafting_table': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'wooden_pickaxe': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'stone': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'furnace': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'stone_pickaxe': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'iron_ore': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'iron_ingot': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'iron_pickaxe': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
            }),
        }),
        'action_space': gym.spaces.Dict({
            "forward": gym.spaces.Discrete(2),
            "back": gym.spaces.Discrete(2),
            "left": gym.spaces.Discrete(2),
            "right": gym.spaces.Discrete(2),
            "jump": gym.spaces.Discrete(2),
            "sneak": gym.spaces.Discrete(2),
            "sprint": gym.spaces.Discrete(2),
            "attack": gym.spaces.Discrete(2),
            "camera": gym.spaces.Box(low=-180, high=180, shape=(2,), dtype=np.float32),  # Pitch, Yaw
            "place": spaces.Enum('none', 'dirt', 'stone', 'crafting_table', 'furnace', 'torch'),
            "craft": spaces.Enum('none', 'torch', 'stick', 'planks'),
            "nearbyCraft": spaces.Enum('none', 'wooden_axe', 'wooden_pickaxe', 'stone_axe', 'stone_pickaxe',
                                       'iron_pickaxe', 'crafting_table', 'furnace'),
            "nearbySmelt": spaces.Enum('none', 'iron_ingot', 'coal')
        })
    },
    max_episode_steps=18000,
)


#######################
#        DEBUG        #
#######################

register(
    id='MineRLNavigateDenseFixed-v0',
    entry_point='minerl.env:MineRLEnv',
    kwargs={
        'xml': os.path.join(missions_dir, 'navigationDenseFixedMap.xml'),
        'observation_space': gym.spaces.Dict({
            'pov': gym.spaces.Box(low=0, high=255, shape=(64,64,3), dtype=np.uint8),
            'inventory': gym.spaces.Dict({
                'dirt': gym.spaces.Box(low=0, high=2304, shape=(1,), dtype=np.int)
            }),
            'compassAngle': gym.spaces.Box(low=-180.0, high=180.0, shape=(1,), dtype=np.float32)
        }),
        'action_space': gym.spaces.Dict({
            "forward": gym.spaces.Discrete(2),
            "back": gym.spaces.Discrete(2),
            "left": gym.spaces.Discrete(2),
            "right": gym.spaces.Discrete(2),
            "jump": gym.spaces.Discrete(2),
            "sneak": gym.spaces.Discrete(2),
            "sprint": gym.spaces.Discrete(2),
            "attack" : gym.spaces.Discrete(2),
            "camera": gym.spaces.Box(low=-180, high=180, shape=(2,), dtype=np.float32),
            "place": spaces.Enum('none', 'dirt')
        }),
    },
    max_episode_steps=6000,
)

register(
    id='MineRLObtainTest-v0',
    entry_point='minerl.env:MineRLEnv',
    kwargs={
        'xml': os.path.join(missions_dir, 'obtainDebug.xml'),
        'observation_space': gym.spaces.Dict({
            'pov': gym.spaces.Box(low=0, high=255, shape=(64, 64, 3), dtype=np.uint8),
            'inventory': gym.spaces.Dict({
                'dirt': gym.spaces.Box(low=0, high=2304, shape=(1,), dtype=np.int),
                'coal': gym.spaces.Box(low=0, high=2304, shape=(1,), dtype=np.int),
                'torch': gym.spaces.Box(low=0, high=2304, shape=(1,), dtype=np.int),
                'log': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'planks': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'stick': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'crafting_table': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'wooden_pickaxe': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'stone': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'furnace': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'stone_pickaxe': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'iron_ore': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'iron_ingot': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
                'iron_pickaxe': gym.spaces.Box(low=0, high=2304, shape=[1], dtype=np.int),
            }),
        }),
        'action_space': gym.spaces.Dict({
            "forward": gym.spaces.Discrete(2),
            "back": gym.spaces.Discrete(2),
            "left": gym.spaces.Discrete(2),
            "right": gym.spaces.Discrete(2),
            "jump": gym.spaces.Discrete(2),
            "sneak": gym.spaces.Discrete(2),
            "sprint": gym.spaces.Discrete(2),
            "attack": gym.spaces.Discrete(2),
            "camera": gym.spaces.Box(low=-180, high=180, shape=(2,), dtype=np.float32),  # Pitch, Yaw
            "place": spaces.Enum('none', 'dirt', 'log', 'cobblestone', 'crafting_table', 'furnace', 'torch'),
            "equip": spaces.Enum('none', 'wooden_axe', 'wooden_pickaxe', 'stone_axe', 'stone_pickaxe',
                                 'iron_pickaxe'),
            "craft": spaces.Enum('none', 'torch', 'stick', 'planks', 'crafting_table'),
            "nearbyCraft": spaces.Enum('none', 'wooden_axe', 'wooden_pickaxe', 'stone_axe', 'stone_pickaxe',
                                       'iron_pickaxe', 'furnace'),
            "nearbySmelt": spaces.Enum('none', 'iron_ingot', 'coal')
        })
    },
    max_episode_steps=18000,
)
