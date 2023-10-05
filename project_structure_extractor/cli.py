#!/usr/bin/env python3

import os
import click

from project_structure_extractor.extractor import extract_structure

@click.command()
@click.option('--path', default='.', help='Path to the project directory.')
@click.option('--hidden-included', is_flag=True, help='Include hidden folders/files in the structure.')
@click.option('--ignore', default='', help='Comma-separated list of files or folders to ignore.')
def cli(path, hidden_included, ignore):
    if not os.path.exists(path):
        click.echo(f"Error: The path {path} does not exist.")
        return

    if not os.path.isdir(path):
        click.echo(f"Error: {path} is not a directory.")
        return

    path = os.path.abspath(path)
    project_name = os.path.basename(path)
    suffix = "_with_hidden" if hidden_included else ""
    output_file_path = os.path.join(os.path.dirname(path), f"{project_name}_structure{suffix}.txt")

    ignore_list = [os.path.abspath(i.strip()) for i in ignore.split(',')] if ignore else []
    ignore_list.append(output_file_path)

    with open(output_file_path, 'w', encoding='utf-8') as file_handle:
        file_handle.write(f"{project_name}/\n")
        extract_structure(path, file_handle, include_hidden=hidden_included, ignore_list=ignore_list)

    click.echo(f"Project structure written to {output_file_path}")

if __name__ == "__main__":
    cli()
