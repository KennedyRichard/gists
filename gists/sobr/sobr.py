### standard library imports

from argparse import ArgumentParser

from pathlib import Path

from itertools import chain

from subprocess import run

from shlex import split


### third-party imports

from textual.app import App, ComposeResult

from textual.containers import Horizontal, Vertical, VerticalScroll

from textual.widgets import Header, Footer, Static, Button, Label

from textual.binding import Binding



DESCRIPTION = "sobr - sound browser to play sound files from current folder"

SOUND_EXTENSIONS = frozenset((
    '.ogg',
    '.wav',
    '.mp3',
))



class TinySoundBrowserApp(App):
    
    CSS = """
    #sidebar {
        dock: left;
        width: 12;
        height: 100%;
    }
    """

    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
    ]

    def __init__(self, directory = '.', volume=70, columns=4):

        super().__init__()

        self.directory = Path(directory)

        self.filenames = sorted(

            path.name
            for path in self.directory.iterdir()

            if path.suffix.lower() in SOUND_EXTENSIONS

        )

        quantity = len(self.filenames)

        if quantity == 0:
            self.no_of_columns = 0

        else:

            if quantity < columns:
                columns = quantity

            no_of_columns = self.no_of_columns = columns

            items_per_column = quantity // no_of_columns

            columns = self.columns = []
            current_column = []
            columns.append(current_column)

            for filename in self.filenames:

                if len(current_column) == items_per_column:

                    current_column = []
                    columns.append(current_column)

                current_column.append(filename)


        self.volume = volume
        self.volume_label = Label(f'Volume: {volume}')

    def compose(self) -> ComposeResult:

        yield Header()
        yield Horizontal(

            Vertical(

                Button("Exit", variant='error', compact=True),
                Static(),
                self.volume_label,
                *(
                    Button(f'{i}', variant='primary', compact=True)
                    for i in range(0, 101, 10)
                ),

                id='sidebar',

            ),

            (

                VerticalScroll(

                    *(
                        Button(filename, variant='success', compact=True)
                        for filename in self.filenames
                    ),

                )

                if self.no_of_columns == 1

                else (

                    Label("No sound files found.")
                    if self.no_of_columns == 0

                    else VerticalScroll(

                        Horizontal(
                            *(

                                Vertical(
                                    *(
                                        Button(filename, variant='success', compact=True)
                                        for filename in column
                                    )
                                )

                                for column in self.columns
                            )

                        )

                    )

                )

            )

        )

        yield Footer()

    def on_mount(self) -> None:

        self.title = 'sobr'
        self.sub_title = 'tiny sound browser'

    def on_button_pressed(self, event: Button.Pressed) -> None:

        button_text = str(event.button.label)

        if isint(button_text):

            volume = self.volume = int(button_text)
            self.volume_label.content = f"Volume: {volume}"

        elif button_text == "Exit":
            self.exit("Leaving app.")

        else:

            filename = str((self.directory / button_text).absolute())

            volume = (

                min(

                    max(

                        0,
                        round(int(self.volume) / 100 * 65536),
                    ),

                    65536,
                )

            )

            run(split(f'paplay "{filename}" --volume={volume}'))
            

def isint(text):

    try:
        int(text)

    except Exception:
        return False

    else:
        return True


if __name__ == "__main__":

    parser = ArgumentParser(description=DESCRIPTION)

    parser.add_argument('-d', '--directory', type=str, default='.')
    parser.add_argument('--volume', type=int, default=70)
    parser.add_argument('--columns', type=int, default=4)

    parsed_args = parser.parse_args()

    directory = parsed_args.directory
    volume = parsed_args.volume
    columns = parsed_args.columns

    app = TinySoundBrowserApp(directory, volume, columns)
    app.run()
