package main

import (
    "context"
    "fmt"
    "log"
    "path/filepath"
    "os"

    "k8s.io/client-go/kubernetes"
    "k8s.io/client-go/tools/clientcmd"
    "k8s.io/client-go/util/homedir"
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

func main() {
    var kubeconfig string
    if home := homedir.HomeDir(); home != "" {
        kubeconfig = filepath.Join(home, ".kube", "config")
    }

    config, err := clientcmd.BuildConfigFromFlags("", kubeconfig)
    if err != nil {
        log.Fatal(err)
    }

    clientset, err := kubernetes.NewForConfig(config)
    if err != nil {
        log.Fatal(err)
    }

    pods, err := clientset.CoreV1().Pods("").List(context.TODO(), metav1.ListOptions{})
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Connected! Found %d pods in cluster\n", len(pods.Items))
    
    for i, pod := range pods.Items {
        if i >= 5 { break } // Just show first 5
        fmt.Printf("- %s/%s\n", pod.Namespace, pod.Name)
    }
}
