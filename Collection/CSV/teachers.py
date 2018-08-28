import csv

with open("Test_results.csv", "a") as csvfile:
    fieldnames = ["test_suite", "test_name", "test_result", "reason", "debug"]
    testwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    testwriter.writeheader()
    testwriter.writerow({'test_suite': 'LOCAL',
        "test_name":"gap_001",
        "test_result": "PASS"
    })
    testwriter.writerow({
        "test_suite": "SERVER",
        "test_name": "RSSI_001",
        "test_result": "FAIL",
        "reason": "not defined"
    })
