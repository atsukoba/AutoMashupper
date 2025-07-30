#!/usr/bin/env python3
"""
Command Line Interface for AutoMashupper
"""

import argparse
import sys
from pathlib import Path


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="AutoMashupper - Automatic mashup generator", prog="automashupper"
    )

    parser.add_argument("--version", action="version", version="automashupper 0.1.0")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Mashability command
    mashability_parser = subparsers.add_parser(
        "mashability", help="Calculate mashability between songs"
    )
    mashability_parser.add_argument("base_song", nargs="?", help="Base song file path")

    # Generate mashup command
    generate_parser = subparsers.add_parser(
        "generate", help="Generate mashup from base song"
    )
    generate_parser.add_argument("base_song", help="Base song file path")

    args = parser.parse_args()

    # Try to import required modules when needed
    if args.command == "mashability":
        try:
            from .mashability import main as mashability_main

            mashability_main(args.base_song)
        except ImportError as e:
            print(f"Error: Required dependencies not available: {e}", file=sys.stderr)
            print(
                "Please ensure all audio processing dependencies are installed.",
                file=sys.stderr,
            )
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "generate":
        try:
            from .mashability import write_songs_mash

            base_song = Path(args.base_song)
            if not base_song.exists():
                print(f"Error: File {base_song} not found", file=sys.stderr)
                sys.exit(1)
            write_songs_mash(str(base_song))
            print(f"Mashup generated successfully for {base_song}")
        except ImportError as e:
            print(f"Error: Required dependencies not available: {e}", file=sys.stderr)
            print(
                "Please ensure all audio processing dependencies are installed.",
                file=sys.stderr,
            )
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
