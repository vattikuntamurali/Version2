#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[ ]:


df = pd.read_csv("/Users/vattikunta/Desktop/ShipSigma/Version2/Book1.csv")


# In[ ]:


df


# In[ ]:


df = df.dropna(subset=['FedExInvoiceDataArchive'])


# In[ ]:


df


# In[ ]:


def clean(strng):
    strng = strng.title()
    strng = strng.replace(" ","")
    strng = strng.replace("-","")
    return strng
    
df['FedExInvoiceCanada'] = df['FedExInvoiceCanada'].map(lambda x: clean(str(x)))


# In[ ]:


def cleaning(strng):
    strng = strng.replace(",[","")
    strng = strng.replace("]","")
    return strng
    
df['FedExInvoiceDataArchive'] = df['FedExInvoiceDataArchive'].map(lambda x: cleaning(str(x)))


# In[ ]:


#df = df.dropna(subset=['FedExInvoiceCanada'])


# In[ ]:


pd.set_option('display.max_columns',200)
pd.set_option('display.max_rows',200)


# In[ ]:


df


# In[ ]:


mapped_data = { 
            "CurrentBalance":"TotalInvoiceDue",
            "Payor":"BillTo",
            "ExpressorGroundTrackingID":"AirWaybillNumber",
            "NetChargeAmount":"AirWaybillTotalAmount",
            "ShipmentDate":"ShipDate" ,
            "PODDeliveryDate":"PodDate",
            "PODSignatureDescription":"PodName",
            "ActualWeightAmount":"ActualWeight",
            "NumberOfPieces":"Pieces",
            "ServicePackaging":"SvcpkgLabel",
            "RecipientName":"RecipientContactName",
            "RecipientCompany":"RecipientCompanyName",
            "RecipientCity":"RecipientAddressCity",
            "RecipientState":"RecipientAddressState",
            "RecipientZipCode":"RecipientAddressPostal",
            "RecipientCountryTerritory":"RecipientAddressCountry/Territory",
            "ShipperCompany":"SenderCompanyName",
            "ShipperName":"SenderContactName",
            "ShipperAddressLine1":"SenderAddressLine1",
            "ShipperAddressLine2":"SenderAddressLine2",
            "ShipperCity":"SenderAddressCity",
            "ShipperState":"SenderAddressState",
            "ShipperZipCode":"SenderAddressPostal",
            "ShipperCountryTerritory":"SenderAddressCountry/Territory",
            "OriginalCustomerReference":"ShipperReference1",
            "OriginalRef2":"ShipperReference2",
            "OriginalRef3PONumber":"ShipperReference3",
            "UpdatedRef2":"UpdatedRef#2",
            "UpdatedRef3PONumber":"UpdatedRef#3/PoNumber",
            "RMA":"Rma#",
            "OriginalRecipientState":"OriginalRecipientState/Province",
            "OriginalRecipientZipCode":"OriginalRecipientZip/PostalCode",
            "OriginalRecipientCountryTerritory":"OriginalRecipientCountry/Territory",
            "AlternateStateProvince":"AlternateState/Province",
            "AlternateZipCode":"AlternateZip/PostalCode",
            "AlternateCountryTerritoryCode":"AlternateCountry/TerritoryCode",
            "CommodityDescription1":"CommodityDescription",
            "CommodityCountryTerritoryCode1":"CommodityCountry/TerritoryCode",
            "CommodityDescription2":"CommodityDescription",
            "CommodityCountryTerritoryCode2":"CommodityCountry/TerritoryCode",
            "CommodityDescription3":"CommodityDescription",
            "CommodityCountryTerritoryCode3":"CommodityCountry/TerritoryCode",
            "CommodityDescription4":"CommodityDescription",
            "CommodityCountryTerritoryCode4":"CommodityCountry/TerritoryCode",
            "TrackingIDChargeDescription1":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount1":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription2":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount2":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription3":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount3":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription4":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount4":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription5":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount5":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription6":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount6":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription7":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount7":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription8":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount8":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription9":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount9":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription10":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount10":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription11":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount11":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription12":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount12":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription13":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount13":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription14":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount14":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription15":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount15":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription16":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount16":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription17":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount17":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription18":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount18":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription19":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount19":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription20":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount20":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription21":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount21":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription22":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount22":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription23":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount23":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription24":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount24":"AirWaybillChargeAmount",
            "TrackingIDChargeDescription25":"AirWaybillChargeLabel",
            "TrackingIDChargeAmount25":"AirWaybillChargeAmount",
            "BillToAccountNumber":"BillToAccountNumber",
            "InvoiceDate":"InvoiceDate",
            "InvoiceNumber":"InvoiceNumber",
            "StoreID":"StoreId",
            "OriginalAmountDue":"OriginalAmountDue",
            "GroundTrackingIDPrefix":"GroundTrackingIdPrefix",
            "TransportationChargeAmount":"TransportationChargeAmount",
            "ServiceType":"ServiceType",
            "GroundService":"GroundService",
            "TenderedDate":"TenderedDate",
            "PODServiceAreaCode":"PodServiceAreaCode",
            "ActualWeightUnits":"ActualWeightUnits",
            "RatedWeightAmount":"RatedWeightAmount",
            "RatedWeightUnits":"RatedWeightUnits",
            "BundleNumber":"BundleNumber",
            "MeterNumber":"MeterNumber",
            "TDMasterTrackingID":"Tdmastertrackingid",
            "DimLength":"DimLength",
            "DimWidth":"DimWidth",
            "DimHeight":"DimHeight",
            "DimDivisor":"DimDivisor",
            "DimUnit":"DimUnit",
            "RecipientAddressLine1":"RecipientAddressLine1",
            "RecipientAddressLine2":"RecipientAddressLine2",
            "OriginalDepartmentReferenceDescription":"OriginalDepartmentReferenceDescription",
            "UpdatedCustomerReference":"UpdatedCustomerReference",
            "UpdatedDepartmentReferenceDescription":"UpdatedDepartmentReferenceDescription",
            "OriginalRecipientAddressLine1":"OriginalRecipientAddressLine1",
            "OriginalRecipientAddressLine2":"OriginalRecipientAddressLine2",
            "OriginalRecipientCity":"OriginalRecipientCity",
            "ZoneCode":"ZoneCode",
            "CostAllocation":"CostAllocation",
            "AlternateAddressLine1":"AlternateAddressLine1",
            "AlternateAddressLine2":"AlternateAddressLine2",
            "AlternateCity":"AlternateCity",
            "CrossRefTrackingIDPrefix":"CrossreftrackingidPrefix",
            "EntryDate":"EntryDate",
            "EntryNumber":"EntryNumber",
            "CustomsValue":"CustomsValue",
            "CustomsValueCurrencyCode":"CustomsValueCurrencyCode",
            "DeclaredValue":"DeclaredValue",
            "DeclaredValueCurrencyCode":"DeclaredValueCurrencyCode",
            "CurrencyConversionDate":"CurrencyConversionDate",
            "CurrencyConversionRate":"CurrencyConversionRate",
            "MultiweightNumber":"MultiweightNumber",
            "MultiweightTotalMultiweightUnits":"MultiweightTotalMultiweightUnits",
            "MultiweightTotalShipmentChargeAmount":"MultiweightTotalShipmentChargeAmount",
            "MultiweightTotalShipmentWeight":"MultiweightTotalShipmentWeight",
            "GroundTrackingIDAddressCorrectionDiscountChargeAmount":"GroundTrackingIdAddressCorrectionDiscountChargeAmount",
            "GroundTrackingIDAddressCorrectionGrossChargeAmount":"GroundTrackingIdAddressCorrectionGrossChargeAmount",
            "ShipmentNotes":"ShipmentNotes",
            "NaN":"Murali"
              }
  
# combining this new data with existing DataFrame
df["CanadaInvoice"] = df["FedExInvoiceDataArchive"].map(mapped_data)


# In[ ]:


for i in df:
    if i == 'FedExInvoiceCanada':
        df = df.drop('FedExInvoiceCanada',axis = 1)


# In[ ]:


#df


# In[ ]:


df1 = pd.DataFrame({"CanadaInvoice": ["ChildAccountNumber", "Currency", "PodTime", "Crossreftrackingid", "MultiweightTotalMultiweightWeight"]})


# In[ ]:


df = df.append(df1, ignore_index=True)


# In[ ]:


df


# In[ ]:


df.to_csv("/Users/vattikunta/Desktop/ShipSigma\version_3.csv", index = False)

