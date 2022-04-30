import React from "react";
//import styled from "styled-components";
import { View, Image, StyleSheet } from 'react-native';
import eatinilogo from "./eatinilogo.jpg";

const Logo = () => {
    return (
        <View>
        <Image
            source={require(eatinilogo)} 
            style={{ width: '100%', height: 150 }}
        />
        {/* <Icon name="logo" 
              style={{
                    position: 'absolute',
                    right: 5,
                    top: 5,
              }} /> */}
    </View> 
    )
}

export default Logo;