from pathlib import Path

import pandas as pd


DEFAULT_INPUT_FILE = "digital_marketing_campaign_dataset_with_creative.csv"
DEFAULT_OUTPUT_FILE = "digital_marketing_campaign_dataset_enriched.csv"


def split_creative_name(input_file: str, output_file: str) -> None:
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        raise FileNotFoundError(f"No se encontro el archivo de entrada: {input_path}")

    df = pd.read_csv(input_path)

    if "CreativeName" not in df.columns:
        raise ValueError("El archivo no contiene la columna requerida: CreativeName")

    creative_parts = df["CreativeName"].str.split("_", expand=True)

    if creative_parts.shape[1] != 5:
        raise ValueError(
            "La columna CreativeName no tiene exactamente 5 componentes "
            "en todas las filas."
        )

    df["Country"] = creative_parts[0]
    df["Platform"] = creative_parts[1]
    df["OperatingSystem"] = creative_parts[2]
    df["Sport"] = creative_parts[3]
    df["Resolution"] = creative_parts[4]

    df.to_csv(output_path, index=False)
    print(f"Archivo generado correctamente: {output_path}")


def main() -> None:
    split_creative_name(DEFAULT_INPUT_FILE, DEFAULT_OUTPUT_FILE)


if __name__ == "__main__":
    main()
