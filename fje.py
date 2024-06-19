import json
import argparse
from factories import *
from explorer import FunnyJsonExplorer

def main():
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', help='<json file>', required=True)
    parser.add_argument('-s', '--style', help='<style>', required=True)
    parser.add_argument('-i', '--icon_family', help='<icon family>', required=True)
    args = parser.parse_args()

    if args.style == 'tree':
        factory = TreeVisualizationFactory(args.icon_family)
    elif args.style == 'rectangle':
        factory = RectangleVisualizationFactory(args.icon_family)
    else:
        raise ValueError('Invalid style')

    explorer = FunnyJsonExplorer(factory)

    with open(args.file, 'r') as f:
        data = json.load(f)

    explorer.load(data)
    explorer.show()

if __name__ == '__main__':
    main()
