import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def load_data():

    folder = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.abspath(os.path.join(
        folder,
        "..",
        "..",
        "data",
        "drop-jump",
        "all_participant_data_rsi.csv"
    ))

    print("Looking for file:", file_path)
    print("File exists:", os.path.exists(file_path))

    data = pd.read_csv(file_path)

    data["participant"] = data["trial"].str.split("_").str[0]

    return data


def paired_rsi_test(data):
    """Compare force plate and accelerometer RSI using a paired t-test."""
    force_values = data["force_plate_rsi"]
    accel_values = data["accelerometer_rsi"]

    # Using paired test.
    t_value, p_value = stats.ttest_rel(force_values, accel_values)

    alpha = 0.05
    print("\nTASK 1: PAIRED T-TEST")
    print("H0: The mean difference between the two methods is zero.")
    print("H1: The mean difference between the two methods is not zero.")
    print("t-value:", round(t_value, 4))
    print("p-value:", p_value)

    if p_value < alpha:
        print("Decision: Reject the null hypothesis.")
        print("There is a statistically significant difference between methods.")
    else:
        print("Decision: Do not reject the null hypothesis.")
        print("There is not enough evidence of a difference between methods.")


def normal_goodness_of_fit(data):
    """Fit a normal curve to accelerometer RSI and run a chi-square test."""
    values = data["accelerometer_rsi"].to_numpy()

    # Estimating the mean and standard deviation from the sample.
    mean_value, std_value = stats.norm.fit(values)

    # 10 bins, including the two open-ended end bins.
    bin_edges = np.r_[
        -np.inf,
        np.linspace(mean_value - 2 * std_value,
                    mean_value + 2 * std_value, 9),
        np.inf
    ]

    observed, _ = np.histogram(values, bins=bin_edges)

    # Probability in each bin.
    probabilities = np.diff(
        stats.norm.cdf(bin_edges, loc=mean_value, scale=std_value)
    )
    expected = probabilities * len(values)
# mean and standard deviation accounted for.
    chi_value, p_value = stats.chisquare(
        observed, f_exp=expected, ddof=2
    )

    print("\nTASK 2: NORMAL DISTRIBUTION GOODNESS-OF-FIT")
    print("Fitted mean:", round(mean_value, 4))
    print("Fitted standard deviation:", round(std_value, 4))
    print("Chi-square statistic:", round(chi_value, 4))
    print("p-value:", p_value)

    if p_value < 0.05:
        print("Conclusion: The normal distribution is not a good fit.")
    else:
        print("Conclusion: The data are reasonably consistent with a normal fit.")

    # histogram and fitted normal probability density curve.
    plt.figure(figsize=(8, 5))
    plt.hist(values, bins=10, density=True, alpha=0.6,
             edgecolor="black", label="Accelerometer RSI")
    x_values = np.linspace(min(values), max(values), 300)
    y_values = stats.norm.pdf(x_values, mean_value, std_value)
    plt.plot(x_values, y_values, linewidth=2,
             label="Fitted normal distribution")
    plt.xlabel("Accelerometer RSI")
    plt.ylabel("Probability density")
    plt.title("Accelerometer RSI and Fitted Normal Distribution")
    plt.legend()
    plt.tight_layout()
    plt.savefig("accelerometer_normal_fit.png")
    plt.show()


def confidence_interval(values):
    """Return the sample mean and 95% t confidence interval."""
    values = np.asarray(values)
    sample_mean = np.mean(values)
    standard_error = stats.sem(values)
    t_critical = stats.t.ppf(0.975, len(values) - 1)
    margin = t_critical * standard_error

    lower = sample_mean - margin
    upper = sample_mean + margin
    return sample_mean, lower, upper


def participant_f_analysis(data):
    """Print Participant F trials and calculate both confidence intervals."""
    participant_f = data[data["participant"] == "F"].copy()

    print("\nTASK 3: PARTICIPANT F")
    print(participant_f[["trial", "force_plate_rsi", "accelerometer_rsi"]])

    force_ci = confidence_interval(participant_f["force_plate_rsi"])
    accel_ci = confidence_interval(participant_f["accelerometer_rsi"])

    print("\nForce plate mean and 95% CI:", force_ci)
    print("Accelerometer mean and 95% CI:", accel_ci)

    # measurements plots across Participant F's trials.
    plt.figure(figsize=(8, 5))
    plt.plot(participant_f["trial"], participant_f["force_plate_rsi"],
             "o-", label="Force plate")
    plt.plot(participant_f["trial"], participant_f["accelerometer_rsi"],
             "s-", label="Accelerometer")
    plt.xlabel("Participant F trial")
    plt.ylabel("Reactive Strength Index (RSI)")
    plt.title("Participant F RSI Measurements")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig("participant_f_comparison.png")
    plt.show()


def main():
    """Run the three assignment tasks."""
    data = load_data()
    print("Number of trials:", len(data))
    paired_rsi_test(data)
    normal_goodness_of_fit(data)
    participant_f_analysis(data)


if __name__ == "__main__":
    main()
