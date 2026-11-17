import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Your Data
file_path = '..\\Resources\\hex_cost_components.csv'
df = pd.read_csv(file_path)

# Define columns for different parameters (Update these based on the actual column names)
columns_of_interest = {
    'Road Construction Costs': [
        'London LH2 road construction costs', 
        'Manchester LH2 road construction costs', 
        'Birmingham LH2 road construction costs', 
        'Glasgow LH2 road construction costs', 
        'Edinburgh LH2 road construction costs', 
        'Cardiff LH2 road construction costs', 
        'Swansea LH2 road construction costs', 
        'Exeter LH2 road construction costs'
    ],
    'Trucking Transport Costs': [
        'London LH2 trucking transport and conversion costs',
        'Manchester LH2 trucking transport and conversion costs',
        'Birmingham LH2 trucking transport and conversion costs',
        'Glasgow LH2 trucking transport and conversion costs',
        'Edinburgh LH2 trucking transport and conversion costs',
        'Cardiff LH2 trucking transport and conversion costs',
        'Swansea LH2 trucking transport and conversion costs',
        'Exeter LH2 trucking transport and conversion costs'
    ],
    'Pipeline Transport Costs': [
        'London LH2 pipeline transport and conversion costs',
        'Manchester LH2 pipeline transport and conversion costs',
        'Birmingham LH2 pipeline transport and conversion costs',
        'Glasgow LH2 pipeline transport and conversion costs',
        'Edinburgh LH2 pipeline transport and conversion costs',
        'Cardiff LH2 pipeline transport and conversion costs',
        'Swansea LH2 pipeline transport and conversion costs',
        'Exeter LH2 pipeline transport and conversion costs'
    ],
    'Production Costs': [
        'London LH2 trucking production cost',
        'Manchester LH2 trucking production cost',
        'Birmingham LH2 trucking production cost',
        'Glasgow LH2 trucking production cost',
        'Edinburgh LH2 trucking production cost',
        'Cardiff LH2 trucking production cost',
        'Swansea LH2 trucking production cost',
        'Exeter LH2 trucking production cost',
        'London LH2 pipeline production cost',
        'Manchester LH2 pipeline production cost',
        'Birmingham LH2 pipeline production cost',
        'Glasgow LH2 pipeline production cost',
        'Edinburgh LH2 pipeline production cost',
        'Cardiff LH2 pipeline production cost',
        'Swansea LH2 pipeline production cost',
        'Exeter LH2 pipeline production cost'
    ],
    'Battery Costs': [
        'London LH2 pipeline battery costs',
        'Manchester LH2 pipeline battery costs',
        'Birmingham LH2 pipeline battery costs',
        'Glasgow LH2 pipeline battery costs',
        'Edinburgh LH2 pipeline battery costs',
        'Cardiff LH2 pipeline battery costs',
        'Swansea LH2 pipeline battery costs',
        'Exeter LH2 pipeline battery costs',
        'London LH2 trucking battery costs',
        'Manchester LH2 trucking battery costs',
        'Birmingham LH2 trucking battery costs',
        'Glasgow LH2 trucking battery costs',
        'Edinburgh LH2 trucking battery costs',
        'Cardiff LH2 trucking battery costs',
        'Swansea LH2 trucking battery costs',
        'Exeter LH2 trucking battery costs'
    ],
    'Solar Costs': [
        'London LH2 pipeline solar costs',
        'Manchester LH2 pipeline solar costs',
        'Birmingham LH2 pipeline solar costs',
        'Glasgow LH2 pipeline solar costs',
        'Edinburgh LH2 pipeline solar costs',
        'Cardiff LH2 pipeline solar costs',
        'Swansea LH2 pipeline solar costs',
        'Exeter LH2 pipeline solar costs',
        'London LH2 trucking solar costs',
        'Manchester LH2 trucking solar costs',
        'Birmingham LH2 trucking solar costs',
        'Glasgow LH2 trucking solar costs',
        'Edinburgh LH2 trucking solar costs',
        'Cardiff LH2 trucking solar costs',
        'Swansea LH2 trucking solar costs',
        'Exeter LH2 trucking solar costs'
    ],
    # Add more categories based on the remaining columns
}

def plot_parameter(df, parameter_name, columns):
    # Filter and melt the DataFrame
    data = df[columns]
    data_melted = data.melt(var_name='City', value_name='Cost')
    
    # Create plot
    plt.figure(figsize=(14, 8))
    sns.barplot(x='City', y='Cost', data=data_melted, errorbar=None, palette='viridis')
    
    # Customize plot
    plt.xticks(rotation=45)
    plt.title(f'{parameter_name} by City')
    plt.xlabel('City')
    plt.ylabel('Cost (£)')
    plt.tight_layout()
    
    # Save the plot
    plot_path = f'D:\\Dissertation\\project\\GeoH2-main\\GeoH2-main\\Resources\\UK\\{parameter_name.replace(" ", "_")}_by_City.png'
    plt.savefig(plot_path)
    plt.show()

# Plot each parameter
for parameter_name, columns in columns_of_interest.items():
    plot_parameter(df, parameter_name, columns)
