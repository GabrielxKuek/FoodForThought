import React, { useState, useEffect } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Modal } from 'react-native';
import { Camera } from 'expo-camera';

const CategoryPage = () => {
  const [hasPermission, setHasPermission] = useState(null);
  const [cameraVisible, setCameraVisible] = useState(false);
  const [cameraRef, setCameraRef] = useState(null);

  // Request permission to use the camera
  useEffect(() => {
    (async () => {
      const { status } = await Camera.requestCameraPermissionsAsync();
      setHasPermission(status === 'granted');
    })();
  }, []);

  const openCamera = () => {
    setCameraVisible(true);
  };

  const closeCamera = () => {
    setCameraVisible(false);
  };

  if (hasPermission === null) {
    return <Text>Requesting for camera permission</Text>;
  }
  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Items in Category</Text>

      {/* Camera Button */}
      <TouchableOpacity style={styles.cameraButton} onPress={openCamera}>
        <Text style={styles.cameraButtonText}>Open Camera</Text>
      </TouchableOpacity>

      {/* Camera Modal */}
      <Modal visible={cameraVisible} animationType="slide">
        <View style={styles.cameraContainer}>
          <Camera
            style={styles.camera}
            ref={(ref) => setCameraRef(ref)}
          >
            <View style={styles.buttonContainer}>
              <TouchableOpacity style={styles.closeButton} onPress={closeCamera}>
                <Text style={styles.closeButtonText}>Close Camera</Text>
              </TouchableOpacity>
            </View>
          </Camera>
        </View>
      </Modal>
    </View>
  );
};

const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'flex-start',
      alignItems: 'center',
    },
    title: {
      fontSize: 24,
      marginVertical: 20,
    },
    cameraButton: {
      position: 'absolute',
      bottom: 30,
      right: 30,
      backgroundColor: 'red',
      borderRadius: 50,
      padding: 15,
      shadowColor: '#000',
      shadowOffset: { width: 0, height: 2 },
      shadowOpacity: 0.8,
      shadowRadius: 2,
      elevation: 5,
    },
    cameraButtonText: {
      color: '#fff',
      fontSize: 16,
    },
    cameraContainer: {
      flex: 1,
      backgroundColor: 'black',
    },
    camera: {
      flex: 1,
    },
    buttonContainer: {
      flex: 1,
      backgroundColor: 'transparent',
      flexDirection: 'row',
      margin: 20,
    },
    closeButton: {
      position: 'absolute',
      bottom: 30,
      left: 30,
      backgroundColor: 'red',
      padding: 10,
      borderRadius: 5,
    },
    closeButtonText: {
      color: '#fff',
      fontSize: 16,
    },
  });

export default CategoryPage;