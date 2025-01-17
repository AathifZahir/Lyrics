# Lyrics Typing Effect

This script simulates the typing effect for the lyrics of the song "Blue Song" by Yung Kai, printing each character of the lyrics with a delay to mimic someone typing them out. It includes delays between each line to create emotional pauses, enhancing the overall experience.

## Features

- **Typing Effect**: Each line is printed character by character with a delay.
- **Customizable Delays**: Character and line delays can be adjusted for each lyric.
- **Smooth Transitions**: Pauses between lines create a natural flow.

## How It Works

1. **Lyrics and Delays**: The lyrics are stored as a list of tuples where each tuple contains a line of the song and the delay for each character in that line.
2. **Line Delays**: After each line is fully printed, a pause is applied before the next line starts, to simulate emotional pacing.
3. **Flush for Immediate Output**: The `flush=True` parameter ensures that each character is printed immediately without buffering.

## Usage

To run the script, simply execute it in your Python environment:

```
python lyrics.py
```

### Example Output:

```
I'll imagine we fell in love
(After a delay)

I'll nap under moonlight skies with you
(After a delay)

I think I'll picture us, you with the waves
(After a delay)

The ocean's colors on your face
(After a delay)

```


## Customization

- **Character Delay**: The delay between each character's appearance can be adjusted by modifying the second value in each tuple in the `lines` list.
- **Line Delay**: The delay between each line of lyrics can be adjusted by changing the values in the `line_delays` list.

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
