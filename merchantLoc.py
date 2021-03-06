import httplib
import urllib,urllib2, urlparse, base64
from oauthlib import oauth1
from lxml import etree

debug=1;

# Returns the Countries
def merchantLocApi(Lat, Lon, pageOffset, pageLength):
    response = ''
    # MASTERCARD PROD CLIENT KEY
    client_key='zwAwpIHtGsALRUt4xWUt44grXpu5Pn460JIz1zUX92b45ce3!644d5a70662b79354746773674725141557847354c413d3d'
    # PROD API ENDPOINT
    #url = "https://api.mastercard.com/merchants/v1/merchant"
    # Sandbox API ENDPOINT
    #url = "https://sandbox.api.mastercard.com/merchants/v1/merchant"
    url = "https://sandbox.api.mastercard.com/merchants/v1/country?Format=XML&Details=acceptance.paypass"

    # SET THE REQUEST PARAMETERS
    params = {
        'Format': "XML",
        'PageLength': pageLength,
        'PageOffset': pageOffset,
        'Country': "USA",
        'latitude': Lat,
        'longitude': Lon,
    }

    # PUT THE URL TOGETHER WITH THE PARAMS
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    # ENCODE THE URL
    url_parts[4] = urllib.urlencode(query)
    
    # THIS IS THE FINAL URL W/PARAMS
    u = urlparse.urlunparse(url_parts)
    
    # BUILD THE REQUEST
    client = oauth1.Client(client_key,
         signature_method=oauth1.SIGNATURE_RSA,
         rsa_key=open('ss.key').read()
         )
    
    # SIGN THE REQUEST
    uri, headers, body = client.sign(u)
    
    # PARSE THE AUTHORIZATION HEADER FOR USE BELOW
    for k,v in headers.iteritems():
        h = "%s" % (v)
    
    # BUILD THE REQUEST HANDLER & OPENER
    handler=urllib2.HTTPSHandler(debuglevel=debug)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener);

      # BUILD THE REQUEST
    request = urllib2.Request(u)
    # ADD THE AUTHORIZATION HEADER
    request.add_header('Authorization',h)
    # SEND THE REQUEST AND READ THE RESULT - ALSO CATCH ERRORS
    try:
        response = urllib2.urlopen(request).read()
    except urllib2.HTTPError, e:
        print ('HTTPError = ' + str(e.code))
    except urllib2.URLError, e:
        print ('URLError = ' + str(e.reason))
    except httplib.HTTPException, e:
        print ('HTTPException')
    except Exception:
        import traceback
        print ('generic exception: ' + traceback.format_exc())
    root = etree.XML( response);
    #transform= etree.XSLT( xslt_root);
    #result = transform( root );
    # print "result io" ,result;
    return response

# Returns the postalCode data
def merchantByPostalCodeApi( postalCode, pageOffset, pageLength  ):
    response = ''
    # MASTERCARD PROD CLIENT KEY
    client_key='zwAwpIHtGsALRUt4xWUt44grXpu5Pn460JIz1zUX92b45ce3!644d5a70662b79354746773674725141557847354c413d3d'
    # PROD API ENDPOINT
    #url = "https://api.mastercard.com/merchants/v1/merchant"
    # Sandbox API ENDPOINT
    #url = "https://sandbox.api.mastercard.com/merchants/v1/merchant"
    url="https://sandbox.api.mastercard.com/atms/v1/atm?Format=XML&PageOffset=0&PageLength=10&AddressLine1=70 Main St&PostalCode=63366&Country=USA&InternationalMaestroAccepted=1"

    # SET THE REQUEST PARAMETERS
    params = {
        'Format': "XML",
        'PageLength': pageLength,
        'PageOffset': pageOffset,
        'PostalCode': postalCode
    }

    # PUT THE URL TOGETHER WITH THE PARAMS
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    # ENCODE THE URL
    url_parts[4] = urllib.urlencode(query)
    
    # THIS IS THE FINAL URL W/PARAMS
    u = urlparse.urlunparse(url_parts)
    
    # BUILD THE REQUEST
    client = oauth1.Client(client_key,
         signature_method=oauth1.SIGNATURE_RSA,
         rsa_key=open('ss.key').read()
         )
    
    # SIGN THE REQUEST
    uri, headers, body = client.sign(u)
    
    # PARSE THE AUTHORIZATION HEADER FOR USE BELOW
    for k,v in headers.iteritems():
        h = "%s" % (v)
    
    # BUILD THE REQUEST HANDLER & OPENER
    handler=urllib2.HTTPSHandler(debuglevel=debug)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener);

      # BUILD THE REQUEST
    request = urllib2.Request(u)
    # ADD THE AUTHORIZATION HEADER
    request.add_header('Authorization',h)
    # SEND THE REQUEST AND READ THE RESULT - ALSO CATCH ERRORS
    try:
        response = urllib2.urlopen(request).read()
    except urllib2.HTTPError, e:
        print ('HTTPError = ' + str(e.code))
    except urllib2.URLError, e:
        print ('URLError = ' + str(e.reason))
    except httplib.HTTPException, e:
        print ('HTTPException')
    except Exception:
        import traceback
        print ('generic exception: ' + traceback.format_exc())
    root = etree.XML( response);
    #transform= etree.XSLT( xslt_root);
    #result = transform( root );
    # print "result io" ,result;
    return response

print "In Merchant Locations"
response=merchantLocApi( 38.7887, 90.5118, 20, 20 );
print "*** Response Follows ***" ;
print response;
# By Postal Code
response=merchantByPostalCodeApi(63366 , 0 , 10);
print response;


