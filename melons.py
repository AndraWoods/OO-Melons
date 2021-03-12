"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    
    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
       

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        
        if self.species == "ChristmasMelon":
            base_price *= 1.5 
        if self.order_type == "International" and self.qty < 10: 
            base_price += 3 
      
        total = (1 + self.tax) * self.qty * base_price
        
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    tax = 0.08
    order_type = 'domestic'

    def __init__(self, species, qty):
        super().__init__(species, qty)
        """Initialize melon order attributes."""

        
        self.shipped = False
        #self.order_type = "domestic"
        #self.tax = 0.08

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    order_type = "international"

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        """Initialize melon order attributes."""
 
        self.country_code = country_code
        self.shipped = False
        
        



    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A U.S Government Tax-Free Melon Order"""
    tax = 0 
    passed_inspection = False 
    order_type = "Government"

    def __init__(self, species, qty):
        super().__init__(species, qty)

        self.marked_inspection = False

    def marked_inspection(self):
        """Indicates if melon passed inspection"""
        if self == "passed":
            passed_inspection = True

      

