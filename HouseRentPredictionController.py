import pandas as pd
from HouseRentPredictor import Regression


class HouseRentPredictionController:
    def __init__(self):
        self.train = pd.read_csv('train.csv')
        self.test = pd.read_csv('test.csv')

    def predict(self, ms_sub_class, ms_zoning, lot_frontage, lot_area, street,lot_shape,
                land_contour, utilities, lot_config, land_slope,house_style, overall_qual,
                overall_cond, year_built, year_remod_add, exter_cond, foundation, gr_liv_area,
                full_bath, bedroom_abv_gr,kitchen_abv_gr, kitchen_qual, tot_rms_abv_grd,
                garage_cars, garage_area, garage_cond, sale_condition):

        linear_regression = Regression(None, None, None, None, None, None, self.train, self.test)
        return linear_regression.predict(ms_sub_class, ms_zoning, lot_frontage, lot_area, street,lot_shape,
                   land_contour, utilities, lot_config, land_slope,house_style, overall_qual,
                   overall_cond, year_built, year_remod_add,exter_cond, foundation, gr_liv_area,
                   full_bath, bedroom_abv_gr,kitchen_abv_gr, kitchen_qual, tot_rms_abv_grd,
                   garage_cars, garage_area, garage_cond, sale_condition)


hp = HouseRentPredictionController()
hp.predict(0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0)
