import csv
from typing import Dict, Optional, Union, List
import pandas as pd


def test_line(line_num: int, row: Dict[str, str]) -> Optional[Dict[str, Union[int, float]]]:
    """
    Clean and validate a single row of package data.
    
    Args:
        line_num: Line number for error reporting
        row: Dictionary containing package dimensions and mass
        
    Returns:
        Dictionary with cleaned and validated data, or None if row is invalid
    """
    cleaned = {}
    required_fields = ['Width', 'Height', 'Length', 'Mass']
    
    # Check for missing required fields
    missing_fields = [field for field in required_fields if field not in row]
    if missing_fields:
        # print(f"Warning: Line {line_num}: Missing required fields: {', '.join(missing_fields)}"
        #       f" - Skipping row")
        return None
    
    # Clean and validate each field
    try:
        # Convert and validate dimensions (must be positive numbers)
        for dim in ['Width', 'Height', 'Length', 'Mass']:
            value = row[dim].strip() if row[dim] else ''
                
            num = float(value)
            if num <= 0:
                raise ValueError("Dimension must be greater than zero")
            cleaned[dim.lower()] = num
        
        return cleaned
        
    except Exception as e:
        # print(f"Error processing line {line_num}: {str(e)}")
        return None


def read_packages(file_path: str) -> List[Dict[str, Union[int, float]]]:
    """
    Read and clean package data from a CSV file.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        List of dictionaries containing cleaned package data
    """
    packages: list[dict] = []
    
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, 1):
                cleaned = test_line(i, row)
                if cleaned:
                    packages.append(cleaned)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
    
    return packages


# if __name__ == "__main__":
#     # Example usage
#     data_path = "src/data/data.csv"
#     packages = read_packages(data_path)
#     print(f"\nSuccessfully processed {len(packages)} packages")
#     if packages:
#         print("\nPackages:", packages)

#     df = pd.DataFrame(packages)
#     print(df)