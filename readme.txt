pytest tests/test_guest_checkout.py --browser=chrome --html=report/test_report_$(date +"%Y%m%d_%H%M").html --self-contained-html

pytest tests/test_guest_checkout.py::TestGuestCheckout::test_guest_checkout --browser=chrome