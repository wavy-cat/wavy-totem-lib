#          Copyright WavyCat 2024 - 2025.
# Distributed under the Boost Software License, Version 1.0.
#        (See accompanying file LICENSE or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

import argparse

from totem_lib import TotemBuilder, SkinType, TopLayers


def check_scale(value):
    int_value = int(value)
    if int_value < 1:
        raise argparse.ArgumentTypeError(f"{value} is an invalid scale! It must be not less than 1.")
    return int_value


# Add parser
parser = argparse.ArgumentParser(description='CLI for totem generation from command line')

parser.add_argument('skin_path', type=str, nargs=1, help='Path to the skin file')
parser.add_argument('totem_path', type=str, nargs=1, help='Path to totem output file')

parser.add_argument('--skin-type', '-t', dest='skin_type', type=str, nargs='?', choices=['wide', 'slim', 'auto'],
                    default='auto', help='Indication of skin type: slim, wide, auto (default: auto)')
parser.add_argument('--top-layers', '-l', dest='top_layers', type=str, nargs='?',
                    choices=['nothing', 'all', 'only_head', 'only_torso', 'only_hands', 'head_and_torso',
                             'head_and_hands'], default='all', help='Zones 2 layers (default: all)')
parser.add_argument('--round-head', '-r', dest='round_head', type=bool, nargs='?', default=False,
                    help='Should the head be rounded at the corners? (default: false)')
parser.add_argument('--scale', '-s', dest='factor', type=check_scale, nargs='?', default=1,
                    help='Totem image scaling factor (default: 1 (without))')

# Parse the arguments
args = parser.parse_args()

skin_path, output_path = args.skin_path[0], args.totem_path[0]
skin_type, top_layers, round_head, scale = args.skin_type, args.top_layers, args.round_head, args.factor
enums = {'skin_type': {'auto': SkinType.SLIM, 'wide': SkinType.WIDE, 'slim': SkinType.SLIM},
         'top_layers': {'nothing': TopLayers.NOTHING, 'all': TopLayers.ALL, 'only_head': TopLayers.ONLY_HEAD,
                        'only_torso': TopLayers.ONLY_TORSO, 'only_hands': TopLayers.ONLY_HANDS,
                        'head_and_torso': TopLayers.HEAD_AND_TORSO, 'head_and_hands': TopLayers.HEAD_AND_HANDS}}

totem = TotemBuilder(skin_path, enums['skin_type'][skin_type], enums['top_layers'][top_layers], round_head)
totem.generate()
if scale > 1:
    totem.scale(factor=scale)
totem.raw.save(output_path)

print('\033[90m[\033[92m✔\033[90m] \033[94mGeneration completed successfully\033[0m')
