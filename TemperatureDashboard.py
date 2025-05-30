"""
🌡️ Elegant Temperature Analysis Dashboard
A sophisticated weather data analysis tool with beautiful visualizations
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configure matplotlib for elegant aesthetics
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

class TemperatureAnalyzer:
    """Sophisticated temperature data analysis and visualization suite"""
    
    def __init__(self, days=30, temp_range=(15, 35), seed=42):
        """Initialize with customizable parameters for reproducible elegance"""
        np.random.seed(seed)
        self.days = days
        self.temperatures = self._generate_realistic_temps(temp_range)
        self.dates = self._generate_date_range()
        
    def _generate_realistic_temps(self, temp_range):
        """Generate more realistic temperature data with natural variations"""
        base_temps = np.random.uniform(temp_range[0], temp_range[1], self.days)
        # Add seasonal trend and daily variations
        trend = np.sin(np.linspace(0, 2*np.pi, self.days)) * 3
        noise = np.random.normal(0, 1.5, self.days)
        return np.clip(base_temps + trend + noise, temp_range[0], temp_range[1])
    
    def _generate_date_range(self):
        """Create elegant date labels"""
        start_date = datetime.now() - timedelta(days=self.days-1)
        return [start_date + timedelta(days=i) for i in range(self.days)]
    
    def analyze_data(self):
        """Comprehensive statistical analysis with elegant presentation"""
        stats = {
            'mean': np.mean(self.temperatures),
            'median': np.median(self.temperatures),
            'std': np.std(self.temperatures),
            'max': np.max(self.temperatures),
            'min': np.min(self.temperatures),
            'range': np.ptp(self.temperatures),
            'warmest_day': np.argmax(self.temperatures) + 1,
            'coldest_day': np.argmin(self.temperatures) + 1,
            'hot_days': np.sum(self.temperatures > 30),
            'cold_days': np.sum(self.temperatures < 20),
            'percentile_75': np.percentile(self.temperatures, 75),
            'percentile_25': np.percentile(self.temperatures, 25)
        }
        return stats
    
    def print_elegant_summary(self):
        """Display analysis results with sophisticated formatting"""
        stats = self.analyze_data()
        
        print("═" * 60)
        print("🌡️  E L E G A N T   T E M P E R A T U R E   A N A L Y S I S")
        print("═" * 60)
        
        print(f"\n📈 STATISTICAL OVERVIEW")
        print("─" * 30)
        print(f"  Mean Temperature    │ {stats['mean']:6.2f}°C")
        print(f"  Median Temperature  │ {stats['median']:6.2f}°C")
        print(f"  Standard Deviation  │ {stats['std']:6.2f}°C")
        print(f"  Temperature Range   │ {stats['range']:6.2f}°C")
        
        print(f"\n🌡️  EXTREME VALUES")
        print("─" * 30)
        print(f"  Maximum Temperature │ {stats['max']:6.2f}°C (Day {stats['warmest_day']})")
        print(f"  Minimum Temperature │ {stats['min']:6.2f}°C (Day {stats['coldest_day']})")
        print(f"  75th Percentile     │ {stats['percentile_75']:6.2f}°C")
        print(f"  25th Percentile     │ {stats['percentile_25']:6.2f}°C")
        
        print(f"\n🔥 CATEGORICAL ANALYSIS")
        print("─" * 30)
        print(f"  Hot Days (>30°C)    │ {stats['hot_days']:6d} days")
        print(f"  Cold Days (<20°C)   │ {stats['cold_days']:6d} days")
        print(f"  Moderate Days       │ {self.days - stats['hot_days'] - stats['cold_days']:6d} days")
        
        print("═" * 60)
    
    def create_elegant_visualization(self):
        """Generate sophisticated multi-panel temperature visualization"""
        fig = plt.figure(figsize=(16, 12))
        gs = fig.add_gridspec(3, 2, height_ratios=[2, 1, 1], hspace=0.3, wspace=0.3)
        
        # Color palette
        colors = {
            'primary': '#2C3E50',
            'secondary': '#E74C3C',
            'accent': '#3498DB',
            'warm': '#F39C12',
            'cool': '#1ABC9C',
            'neutral': '#95A5A6'
        }
        
        # Main temperature trend
        ax1 = fig.add_subplot(gs[0, :])
        self._plot_main_trend(ax1, colors)
        
        # Temperature distribution
        ax2 = fig.add_subplot(gs[1, 0])
        self._plot_distribution(ax2, colors)
        
        # Moving average
        ax3 = fig.add_subplot(gs[1, 1])
        self._plot_moving_average(ax3, colors)
        
        # Heat map calendar
        ax4 = fig.add_subplot(gs[2, :])
        self._plot_temperature_heatmap(ax4, colors)
        
        plt.suptitle(
            '🌡️ Sophisticated Temperature Analysis Dashboard',
            fontsize=20, fontweight='bold', y=0.98,
            color=colors['primary']
        )
        
        plt.tight_layout()
        plt.show()
    
    def _plot_main_trend(self, ax, colors):
        """Elegant main temperature trend visualization"""
        days_range = np.arange(1, self.days + 1)
        
        # Temperature line with gradient effect
        ax.plot(days_range, self.temperatures, 
                linewidth=3, color=colors['primary'], 
                marker='o', markersize=6, markerfacecolor=colors['accent'],
                markeredgecolor='white', markeredgewidth=1.5,
                label='Daily Temperature', alpha=0.8)
        
        # Statistical lines
        mean_temp = np.mean(self.temperatures)
        ax.axhline(y=mean_temp, color=colors['warm'], 
                  linestyle='--', linewidth=2, alpha=0.8,
                  label=f'Mean ({mean_temp:.1f}°C)')
        
        # Confidence bands
        std_temp = np.std(self.temperatures)
        ax.fill_between(days_range, mean_temp - std_temp, mean_temp + std_temp,
                       alpha=0.2, color=colors['neutral'], 
                       label='±1 Standard Deviation')
        
        # Styling
        ax.set_title('Daily Temperature Trend Analysis', 
                    fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Day of Month', fontsize=12, fontweight='bold')
        ax.set_ylabel('Temperature (°C)', fontsize=12, fontweight='bold')
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend(loc='upper right', framealpha=0.9)
        ax.set_xlim(1, self.days)
    
    def _plot_distribution(self, ax, colors):
        """Temperature distribution histogram"""
        ax.hist(self.temperatures, bins=12, alpha=0.7, 
               color=colors['accent'], edgecolor='white', linewidth=1.5)
        ax.axvline(np.mean(self.temperatures), color=colors['secondary'], 
                  linestyle='--', linewidth=2, label='Mean')
        ax.set_title('Temperature Distribution', fontweight='bold')
        ax.set_xlabel('Temperature (°C)')
        ax.set_ylabel('Frequency')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_moving_average(self, ax, colors):
        """7-day moving average trend"""
        if self.days >= 7:
            window = min(7, self.days // 2)
            moving_avg = np.convolve(self.temperatures, 
                                   np.ones(window)/window, mode='valid')
            days_ma = np.arange(window, self.days + 1)
            
            ax.plot(days_ma, moving_avg, 
                   linewidth=3, color=colors['cool'],
                   marker='s', markersize=4)
            ax.set_title(f'{window}-Day Moving Average', fontweight='bold')
            ax.set_xlabel('Day')
            ax.set_ylabel('Temperature (°C)')
            ax.grid(True, alpha=0.3)
    
    def _plot_temperature_heatmap(self, ax, colors):
        """Calendar-style temperature heatmap"""
        # Reshape data for calendar view
        weeks = (self.days + 6) // 7
        cal_data = np.full((weeks, 7), np.nan)
        
        for i, temp in enumerate(self.temperatures):
            week = i // 7
            day = i % 7
            if week < weeks:
                cal_data[week, day] = temp
        
        # Create heatmap
        im = ax.imshow(cal_data, cmap='RdYlBu_r', aspect='auto', 
                      vmin=np.min(self.temperatures), 
                      vmax=np.max(self.temperatures))
        
        # Styling
        ax.set_title('Temperature Calendar Heatmap', fontweight='bold', pad=10)
        ax.set_xticks(range(7))
        ax.set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
        ax.set_yticks(range(weeks))
        ax.set_yticklabels([f'Week {i+1}' for i in range(weeks)])
        
        # Add colorbar
        cbar = plt.colorbar(im, ax=ax, shrink=0.8)
        cbar.set_label('Temperature (°C)', rotation=270, labelpad=20)

def main():
    """Execute the elegant temperature analysis"""
    print("🚀 Initializing Elegant Temperature Analysis...")
    
    # Create analyzer instance
    analyzer = TemperatureAnalyzer(days=30, temp_range=(15, 35))
    
    # Display elegant summary
    analyzer.print_elegant_summary()
    
    # Generate sophisticated visualizations
    print("\n🎨 Generating sophisticated visualizations...")
    analyzer.create_elegant_visualization()
    
    print("\n✨ Analysis complete! Enjoy your elegant temperature insights.")

if __name__ == "__main__":
    main()
