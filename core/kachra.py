# akp2 =  (df['types'].str.contains('Hunting', na=False)) | (df['types'].str.contains('Horse', na=False)) | (
            # df['types'].str.contains('House', na=False)) | (df['types'].str.contains('Lakefront', na=False)) | (
            #        df['types'].str.contains('Farms and Ranches', na=False)) | (
        akp2 = (df['types'] == types)
        # if types== 'Farms and Ranches' or types== 'Hunting' or types== 'Horse' or types== 'House' or types== 'Lakefront' or types=='Farms and Ranches'  or types=='Recreational' or types=='Oceanfront' or types=='Waterfront' :
        #     print("akp")
        dp = df['state'] == "Texas"
        akp3 = (df['status'] == status)
        # dp = df['state'] == "Texas"
        # if any(akp) :
        #     print("Ram JIIII is Great")
        #     dp = akp
        # else :
        #     print("Shyam JIIII is GReat")
        print("Bharat Bhiyaa",types)
        #
        # if types != None:
        #     print("Ashish Bhiyaa")
        #     dp = akp2
        # else :
        #     print("Nirupama Rai")


# newdf = df.loc[(df.state == "Texas") & (df.county == "Edwards County")]
# data2 = []
# data2 = json.loads(json_records)
# print(newdf)




Anji

if types is not None:
        print("nlp", types)
        akp2 = (df['types'].str.contains('Hunting', na=False)) & (df['types'].str.contains('House', na=False)) & (
                df['types'].str.contains('Farms and Ranches', na=False))
        dp = akp2
        akp3 = (df['types'].str.contains('Recreational ', na=False)) & (
                df['types'].str.contains('Farms and Ranches ', na=False)) & (
                       df['types'].str.contains('Hunting', na=False))
        dp = akp3
        akp4 = (df['types'].str.contains('Hunting', na=False)) & (df['types'].str.contains('House', na=False)) & (
                df['types'].str.contains('Farms and Ranches', na=False))
        dp = akp4
        akp5 = (df['types'].str.contains('Recreational ', na=False)) & (
                df['types'].str.contains('Farms and Ranches ', na=False)) & (
                       df['types'].str.contains('Hunting', na=False))
        dp = akp5
        akp7 = (df['types'].str.contains('Timberland ', na=False)) | (
                df['types'].str.contains('Farms and Ranches ', na=False)) | (
                       df['types'].str.contains('Hunting', na=False))
        dp = akp7
        akp7 = (df['types'].str.contains('Timberland ', na=False)) & (
                df['types'].str.contains('Farms and Ranches ', na=False)) & (
                       df['types'].str.contains('Hunting', na=False))
        dp = akp7
        akp6 = (df['types'].str.contains('Timberland', na=False)) | (df['types'].str.contains('House', na=False)) | (
                df['types'].str.contains('Farms and Ranches', na=False))
        dp = akp6
        akp7 = (df['types'].str.contains('Recreational ', na=False)) | (
                df['types'].str.contains('Farms and Ranches ', na=False)) | (
                       df['types'].str.contains('Hunting', na=False))
        dp = akp7
        akp7 = (df['types'].str.contains('Timberland ', na=False)) | (
                df['types'].str.contains('Farms and Ranches ', na=False)) | (
                       df['types'].str.contains('Hunting', na=False))
else:
        print("Type is NA")
if status is not None:
        akp8 = (df['status'] == status)
        # print(akp8)
        dp = akp8
else:
        print("Status is NA")
if view_acres is not None:
        try:
                akp9 = (df['acres'] <= float(view_acres))
                dp = akp9
        except:
                print("Hello World")
                akp = (df['state'] == title_contains_query) | (df['city'] == title_contains_query) | (
                        df['county'] == title_contains_query)
                dp = akp
                print("nlp", types)
                akp2 = (df['types'].str.contains('Hunting', na=False)) & (
                        df['types'].str.contains('House', na=False)) & (
                               df['types'].str.contains('Farms and Ranches', na=False))
                dp = akp2
                akp3 = (df['types'].str.contains('Recreational ', na=False)) & (
                        df['types'].str.contains('Farms and Ranches ', na=False)) & (
                               df['types'].str.contains('Hunting', na=False))
                dp = akp3
                akp4 = (df['types'].str.contains('Hunting', na=False)) & (
                        df['types'].str.contains('House', na=False)) & (
                               df['types'].str.contains('Farms and Ranches', na=False))
                dp = akp4
                akp5 = (df['types'].str.contains('Recreational ', na=False)) & (
                        df['types'].str.contains('Farms and Ranches ', na=False)) & (
                               df['types'].str.contains('Hunting', na=False))
                dp = akp5
                akp7 = (df['types'].str.contains('Timberland ', na=False)) | (
                        df['types'].str.contains('Farms and Ranches ', na=False)) | (
                               df['types'].str.contains('Hunting', na=False))
                dp = akp7
                akp7 = (df['types'].str.contains('Timberland ', na=False)) & (
                        df['types'].str.contains('Farms and Ranches ', na=False)) & (
                               df['types'].str.contains('Hunting', na=False))
                dp = akp7
                akp6 = (df['types'].str.contains('Timberland', na=False)) | (
                        df['types'].str.contains('House', na=False)) | (
                               df['types'].str.contains('Farms and Ranches', na=False))
                dp = akp6
                akp7 = (df['types'].str.contains('Recreational ', na=False)) | (
                        df['types'].str.contains('Farms and Ranches ', na=False)) | (
                               df['types'].str.contains('Hunting', na=False))
                dp = akp7
                akp7 = (df['types'].str.contains('Timberland ', na=False)) | (
                        df['types'].str.contains('Farms and Ranches ', na=False)) | (
                               df['types'].str.contains('Hunting', na=False))

else:
        print("Area is NA")