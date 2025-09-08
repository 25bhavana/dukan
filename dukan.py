import streamlit as st

# शीर्षक
st.title("दूध का हिसाब")

# वस्तुओं की कीमतें (प्रति यूनिट)
rates = {
    "अहार": 54.25,
    "सर्वोत्तम": 68,
    "पनीर 1kg": 250,
    "पनीर पैकेटवाला": 82,
    "दही 200 ग्राम": 17,
    "मटर 1kg": 90,
    "स्टार": 51,
    "गोल्ड": 56,
    "राजन्स": 54,
    "छोटा दूध": 45,
    "दही 400 ग्राम": 32,
    "दही 5kg": 250
}

# सप्लायर टैब्स
tabs = st.tabs(["जाफर", "पंडितजी", "देवगडे"])

# जाफर
with tabs[0]:
    st.header("जाफर से वस्तुएँ")
    ahar = st.number_input("अहार (लीटर)", min_value=0, key="jaffer_ahar")
    sarvottam = st.number_input("सर्वोत्तम (लीटर)", min_value=0, key="jaffer_sarvottam")
    paneer_1kg = st.number_input("पनीर 1kg ", min_value=0, key="jaffer_paneer1")
    paneer_packet = st.number_input("पनीर पैकेटवाला", min_value=0, key="jaffer_paneer_packet")
    dahi_200 = st.number_input("दही 200 ग्राम (पैकेट)", min_value=0, key="jaffer_dahi200")
    matar = st.number_input("मटर 1kg (किलोग्राम)", min_value=0, key="jaffer_matar")
    rajans = st.number_input("राजन्स (लीटर)", min_value=0, key="jaffer_rajans")
    chota_doodh = st.number_input("छोटा दूध (लीटर)", min_value=0, key="jaffer_chota")

    total_jaffer = (
        ahar * rates["अहार"] +
        sarvottam * rates["सर्वोत्तम"] +
        paneer_1kg * rates["पनीर 1kg"] +
        paneer_packet * rates["पनीर पैकेटवाला"] +
        dahi_200 * rates["दही 200 ग्राम"] +
        matar * rates["मटर 1kg"] +
        rajans * rates["राजन्स"] +
        chota_doodh * rates["छोटा दूध"]
    )

    st.subheader(f"जाफर कुल: ₹ {total_jaffer:.2f}")

# पंडितजी
with tabs[1]:
    st.header("पंडितजी से वस्तुएँ")
    star = st.number_input("स्टार (लीटर)", min_value=0, key="pandit_star")
    gold = st.number_input("गोल्ड (लीटर)", min_value=0, key="pandit_gold")
    rajans2 = st.number_input("राजन्स (लीटर)", min_value=0, key="pandit_rajans")
    chota_doodh2 = st.number_input("छोटा दूध (लीटर)", min_value=0, key="pandit_chota")

    total_pandit = (
        star * rates["स्टार"] +
        gold * rates["गोल्ड"] +
        rajans2 * rates["राजन्स"] +
        chota_doodh2 * rates["छोटा दूध"]
    )

    st.subheader(f"पंडितजी कुल: ₹ {total_pandit:.2f}")

# देवगडे
with tabs[2]:
    st.header("देवगडे से वस्तुएँ")
    dahi_400_dev = st.number_input("दही 400 ग्राम (पैकेट)", min_value=0, key="dev_400")
    matar_dev = st.number_input("मटर 1kg (किलोग्राम)", min_value=0, key="dev_matar")
    dahi_5kg = st.number_input("दही 5kg (किलोग्राम)", min_value=0, key="dev_5kg")
    rajans3 = st.number_input("राजन्स (लीटर)", min_value=0, key="dev_rajans")
    chota_doodh3 = st.number_input("छोटा दूध (लीटर)", min_value=0, key="dev_chota")

    total_devgade = (
        dahi_400_dev * rates["दही 400 ग्राम"] +
        matar_dev * rates["मटर 1kg"] +
        dahi_5kg * rates["दही 5kg"] +
        rajans3 * rates["राजन्स"] +
        chota_doodh3 * rates["छोटा दूध"]
    )

    st.subheader(f"देवगडे कुल: ₹ {total_devgade:.2f}")

# अंतिम कुल
grand_total = total_jaffer + total_pandit + total_devgade
st.markdown("---")
st.header(f"संपूर्ण कुल राशि: ₹ {grand_total:.2f}")
