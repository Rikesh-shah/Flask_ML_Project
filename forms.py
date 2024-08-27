import pandas as pd
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import (
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField
)

# loading the csv data to populate the drop downs
train = pd.read_csv("data/train.csv")
val = pd.read_csv("data/val.csv")
X_data = pd.concat([train, val], axis=0).drop(columns="price")

dataRequired = DataRequired()

class InputForm(FlaskForm):
    airline = SelectField(
        label="Airline",
        choices=X_data.airline.unique().tolist(),
        validators=[dataRequired]
    )
    date_of_journey = DateField(
        label="Date of Journey",
        validators=[dataRequired]
    )
    source = SelectField(
        label="Source",
        choices=X_data.source.unique().tolist(),
        validators=[dataRequired]
    )
    destination = SelectField(
        label="Destination",
        choices=X_data.destination.unique().tolist(),
        validators=[dataRequired]
    )
    dep_time = TimeField(
        label="Departure Time",
        validators=[dataRequired]
    )
    arrival_time = TimeField(
        label="Arrival Time",
        validators=[dataRequired]
    )
    duration = IntegerField(
        label="Duration",
        validators=[dataRequired]
    )
    total_stops = IntegerField(
        label="Total Stops",
        validators=[dataRequired]
    )
    additional_info = SelectField(
        label="Additional Info",
        choices=X_data.additional_info.unique().tolist(),
        validators=[dataRequired]
    )
    submit = SubmitField("Predict")