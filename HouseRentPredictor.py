import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline


class Regression:

    def __init__(self, train1, x_train, x_test, y_train, y_test, labels, train, test):
        self.train1 = train1
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test
        self.labels = labels
        self.train = train
        self.test = test
        self.model = LinearRegression()

    def __drop_columns(self):
        self.train1 = self.train.drop(['Id', 'Alley', 'Neighborhood', 'Condition1',
                    'Condition2', 'BldgType', 'RoofStyle',
                    'RoofMatl', 'Exterior1st', 'Exterior2nd',
                    'MasVnrType', 'MasVnrArea', 'ExterQual',
                    'BsmtQual', 'BsmtCond', 'BsmtExposure',
                    'BsmtFinType1', 'BsmtFinSF1', 'BsmtFinType2',
                    'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF',
                    'Heating', 'HeatingQC', 'CentralAir',
                    'Electrical', '1stFlrSF', '2ndFlrSF',
                    'LowQualFinSF', 'BsmtFullBath',
                    'BsmtHalfBath', 'HalfBath', 'Functional',
                    'Fireplaces', 'FireplaceQu', 'GarageType',
                    'GarageYrBlt', 'GarageFinish', 'GarageQual',
                    'PavedDrive', 'WoodDeckSF', 'OpenPorchSF',
                    'EnclosedPorch', '3SsnPorch', 'ScreenPorch',
                    'PoolArea', 'PoolQC', 'Fence',
                    'MiscFeature', 'MiscVal', 'MoSold',
                    'YrSold', 'SaleType'], axis=1)

    def __convert_to_number(self):
        self.train1 = self.train1.astype(str)
        self.train1['MSSubClass'] = self.train1.MSSubClass.map({'180': 1, '30': 2, '45': 2, '190': 3, '50': 3, '90': 3,
                                                                '85': 4, '40': 4, '160': 4, '70': 5, '20': 5, '75': 5,
                                                                '80': 5, '150': 5, '120': 6, '60': 6})
        self.train1['MSZoning'] = self.train1.MSZoning.map({'C (all)': 1, 'RH': 2, 'RM': 2, 'RL': 3, 'FV': 4})
        self.train1['Street'] = self.train1.Street.map({'Pave': 1, 'Grvl': 2})
        self.train1['LotShape'] = self.train1.LotShape.map({'Reg': 1, 'IR1': 2, 'IR2': 3, 'IR3': 4})
        self.train1['LandContour'] = self.train1.LandContour.map({'Lvl': 1, 'Bnk': 2, 'HLS': 3, 'Low': 4})
        self.train1['Utilities'] = self.train1.Utilities.map({'AllPub': 1, 'NoSewr': 2, 'NoSeWa': 3, 'ELO': 4})
        self.train1['LotConfig'] = self.train1.LotConfig.map({'Inside': 1, 'Corner': 2, 'CulDSac': 3, 'FR2': 4, 'FR3': 5})
        self.train1['LandSlope'] = self.train1.LandSlope.map({'Gtl': 1, 'Mod': 2, 'Sev': 3})
        self.train1['HouseStyle'] = self.train1.HouseStyle.map(
                {'1Story': 1, '1.5Fin': 2, '1.5Unf': 3, '2Story': 4, '2.5Fin': 5, '2.5Unf': 6, 'SFoyer': 7, 'SLvl': 8})
        self.train1['ExterCond'] = self.train1.ExterCond.map({'Ex': 1, 'Gd': 2, 'TA': 3, 'Fa': 4, 'Po': 5})
        self.train1['Foundation'] = self.train1.Foundation.map(
                {'BrkTil': 1, 'CBlock': 2, 'PConc': 3, 'Slab': 4, 'Stone': 5, 'Wood': 6})
        self.train1['KitchenQual'] = self.train1.KitchenQual.map({'Ex': 1, 'Gd': 2, 'TA': 3, 'Fa': 4, 'Po': 5})
        self.train1['GarageCond'] = self.train1.GarageCond.map({'Ex': 1, 'Gd': 2, 'TA': 3, 'Fa': 4, 'Po': 5, 'NA': 6})
        self.train1['SaleCondition'] = self.train1.SaleCondition.map(
                {'Normal': 1, 'Abnorml': 2, 'AdjLand': 3, 'Alloca': 4, 'Family': 5, 'Partial': 6})

    def __clean_up(self):
        self.train1.dropna(inplace=True)
        self.train1 = self.train1[self.train1.LotFrontage != 'nan']

    def __create_labels(self):
        self.labels = self.train1['SalePrice']
        self.train1 = self.train1.drop(['SalePrice'], axis=1)

    def __split_data(self):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.train1, self.labels, test_size= 0.010, random_state=2)

    def __train_model(self):
        self.model.fit(self.x_train, self.y_train)

    def predict(self, ms_sub_class, ms_zoning, lot_frontage, lot_area, street,lot_shape,
                land_contour, utilities, lot_config, land_slope,house_style, overall_qual,
                overall_cond, year_built, year_remod_add,exter_cond, foundation, gr_liv_area,
                full_bath, bedroom_abv_gr,kitchen_abv_gr, kitchen_qual, tot_rms_abv_grd, garage_cars,garage_area, garage_cond, sale_condition):
        self.__drop_columns()
        self.__convert_to_number()
        self.__clean_up()
        self.__create_labels()
        self.__split_data()
        self.__train_model()
        input_data = self.x_test.head(0)
        input_data.loc[0] = [ms_sub_class, ms_zoning, lot_frontage, lot_area, street,lot_shape,
                                         land_contour, utilities, lot_config, land_slope,house_style, overall_qual,
                                         overall_cond, year_built, year_remod_add,exter_cond, foundation, gr_liv_area,
                                         full_bath, bedroom_abv_gr,kitchen_abv_gr, kitchen_qual, tot_rms_abv_grd,
                                         garage_cars, garage_area, garage_cond, sale_condition]
        print(input_data)
        return self.model.predict(input_data)

