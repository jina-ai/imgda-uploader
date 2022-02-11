import argparse
import os.path
import secrets

from docarray import DocumentArray, Document
from rich.console import Console
from rich.progress import track
from rich.syntax import Syntax

parser = argparse.ArgumentParser(description='Image Uploader')
parser.add_argument(
    'folder', type=str, help='all images from that folder will be uploaded'
)
parser.add_argument(
    '--shape', type=int, metavar='N', default=224, help='reshape all images to N x N'
)
parser.add_argument(
    '--normalize', action='store_true', help='normalize the image in preprocessing'
)
parser.add_argument(
    '--channel-first', action='store_true', help='bring channel axis from last to first'
)
parser.add_argument(
    '--glob-pattern',
    action='append',
    nargs='+',
    type=str,
    default=['**/*.jpg', '**/*.png'],
    help='the pattern for image files',
)
parser.add_argument(
    '--token',
    help='token for later DocumentArray access, when not given will auto generate a 8-length one',
)


def preprocess(args):
    def preproc(d: Document):
        if args.shape:
            d = d.load_uri_to_image_tensor(width=args.shape, height=args.shape)
        else:
            d = d.load_uri_to_image_tensor()
        if args.normalize:
            d.set_image_tensor_normalization()
        if args.channel_first:
            d.set_image_tensor_channel_axis(-1, 0)
        return d

    path = os.path.abspath(args.folder)
    glob = [os.path.join(path, g) for g in args.glob_pattern]
    console = Console(force_terminal=True, force_interactive=True)
    if not args.token:
        args.token = secrets.token_urlsafe(8)
        console.print(f'Your token will be: [green]{args.token}[/green]')

    with console.status(f'Collecting [bold]{glob}[/bold]...') as status:
        da = DocumentArray.from_files(glob)
        status.update(f'{len(da)} Documents')

    for _ in track(da.map(preproc), total=len(da), description='Preprocessing'):
        pass

    da.push(args.token, show_progress=True)
    console.print(':tada: [green]Success![/green] Here is how you can use it:')
    my_code = f'''
from docarray import DocumentArray

da = DocumentArray.pull('{args.token}')
    '''
    syntax = Syntax(my_code, 'python', theme='monokai', line_numbers=True)
    console.print(syntax)


if __name__ == '__main__':
    args = parser.parse_args()
    preprocess(args)
