import requests
import bs4

class Turkish:
    
    def __init__(self, data):
        self.totalFare = data["totalFare"]
        self.baseFare = data["baseFare"]
        self.totalTaxes = self.totalFare-self.baseFare
        self.taxes = data["taxes"]
        self.dates = data["dates"]
        self.company_codes = data["company_codes"]
        self.currencies = data["currencies"]
        self.rules = data["rules"]
        self.ticketStatus = "OK"
    
    def calculate(self):            
        rules = self.rules.split("\n")
        cancellation = []
        penalty = []
        non_refunded_tax = 0
        non_refunded_taxes = []
        refunded_taxes = 0
        check = 0
        for rule in rules:
            if "CHANGES" in rule:
                check = 1
            elif "CANCELLATIONS" in rule:
                check = 2
            if check == 2:
                cancellation.append(rule)
        
        check = 0
        for rule in cancellation:
            if "NO-SHOW" in rule and "NON-REFUNDABLE" in rule:
                if self.ticketStatus == "NO-SHOW":
                    if not self.dates[0] < self.dates[1]:
                        return None
            if "SURCHARGE" in rule or "TAX" in rule:
                for tax in self.taxes:
                    if tax["Type"] in rule:
                        non_refunded_taxes.append(tax)
            if "BEFORE DEPARTURE" in rule:
                check = 1
            elif "AFTER DEPARTURE" in rule:
                check = 2
            if check == 1:
                if "CANCEL/REFUND" in rule:
                    for r in rule.split():
                        if r=="USD" or r=="EUR":
                            penalty.append(r)
                        try:
                            penalty.append(float(r))
                        except:
                            pass
        non_refunded_tax = self.__non_refundable_taxes(non_refunded_taxes)

        non_ref_fare = round(self.__get_Exchange_Rates(penalty), 1)

        if non_refunded_taxes == 0:
            refunded_taxes = self.totalTaxes
        else:
            refunded_taxes = self.totalTaxes - non_refunded_tax
        
        output = {
            'non_refundable taxes': non_refunded_tax,
            'penalty': str(penalty[1])+" "+penalty[0]+" or "+str(non_ref_fare)+" "+"KZT",
            'refunded_fare': self.baseFare - non_ref_fare,
            'refunded_taxes':  refunded_taxes,
            'refunded_total': (self.baseFare-non_ref_fare)+refunded_taxes,
            'name': "Turkish AirLine",
            'currency': self.currencies
        }
        return output

    def __non_refundable_taxes(self, taxes):
        amount = 0
        for tax in taxes:
            amount += tax["Amount"]
        return amount

    def __get_Exchange_Rates(self, data):
        site = requests.get('https://prodengi.kz/currency/')
        html = bs4.BeautifulSoup(site.text, "html.parser")
        if data[0]=="EUR" or data[0]=="RUB" or data[0]=="USD":
            tenge = html.select('.content_list .'+data[0]+' .price_buy')
            out = tenge[0].getText()
            out = float(out) * float(data[1])
        return out