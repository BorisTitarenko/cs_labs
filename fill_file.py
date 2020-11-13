string = "So close, no matter how far\n" \
         "Couldn't be much more from the heart" \
         "\nForever trusting who we are" \
         "\nAnd nothing else matters" \
         "\nNever opened myself this way" \
         "\nLife is ours, we live it our way" \
         "\nAll these words I don't just say" \
         "\nAnd nothing else matters\n" \
         "Trust I seek and I find in you" \
         "\nEvery day for us something new" \
         "\nOpen mind for a different view" \
         "\nAnd nothing else matters" \
         "\nNever cared for what they do" \
         "\nNever cared for what they know" \
         "\nBut I know" \
         "\nSo close, no matter how far" \
         "\nCouldn't be much more from the heart" \
         "\nForever trusting who we are" \
         "\nAnd nothing else matters" \
         "\nNever cared for what they do" \
         "\nNever cared for what they know" \
         "\nBut I know" \
         "\nI never opened myself this way" \
         "\nLife is ours, we live it our way" \
         "\nAll these words I don't just say" \
         "\nAnd nothing else matters" \
         "\nTrust I seek and I find in you" \
         "\nEvery day for us, something new" \
         "\nOpen mind for a different view" \
         "\nAnd nothing else matters" \
         "\nNever cared for things they say" \
         "\nNever cared for games they play" \
         "\nNever cared for what they do" \
         "\nNever cared for what they know" \
         "\nAnd I know, yeah!" \
         "\nSo close, no matter how far" \
         "\nCouldn't be much more from the heart" \
         "\nForever trusting who we are" \
         "\nNo, nothing else matters"

b = bytearray([ord(i) for i in string])
with open("input.txt", "wb") as f:
    f.write(b)